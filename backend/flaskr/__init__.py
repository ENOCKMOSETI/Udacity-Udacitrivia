import os
import sys
from flask import Flask, flash, render_template, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  db = SQLAlchemy(app)
  '''
  @TODO: Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
  '''
  cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

  '''
  @TODO: Use the after_request decorator to set Access-Control-Allow
  '''
  @app.after_request
  def after_request(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "POST, GET, PUT, DELETE"
    response.headers["Access-Control-Allow-Headers"] = "Accept, Content-Type, Content-Length, Accept-Encoding, X_XSRF-Token"
    return response

  def paginateQuestions(request, questions):
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE
    questions = Question.query.all()
    formattedQuestions = [question.format() for question in questions]
    return formattedQuestions[start:end]
  '''
  @TODO: 
  Create an endpoint to handle GET requests 
  for all available categories.
  '''
  @app.route('/categories', methods=['GET'])
  def get_categories():
    categories = Category.query.all()
    categories_list = [category.type for category in categories]
    if len(categories_list) == 0:
      abort(404)
    return jsonify({
      'success': True,
      'categories': categories_list
    })

  '''
  @TODO: 
  Create an endpoint to handle GET requests for questions, 
  including pagination (every 10 questions). 
  This endpoint should return a list of questions, 
  number of total questions, current category, categories. 

  TEST: At this point, when you start the application
  you should see questions and categories generated,
  ten questions per page and pagination at the bottom of the screen for three pages.
  Clicking on the page numbers should update the questions. 
  '''
  @app.route('/questions', methods=['GET'])
  def get_questions():
    questions = Question.query.order_by(Question.id).all()
    formattedQuestions = paginateQuestions(request, questions)
    if len(formattedQuestions) == 0:
      abort(404)
    categories = Category.query.all()
    categories_list = [category.type for category in categories]
    return jsonify({
      'success': True,
      'questions': formattedQuestions,
      'total_questions': len(questions),
      'categories': categories_list,
      'current_category': None
    })
  '''
  @TODO: 
  Create an endpoint to DELETE question using a question ID. 

  TEST: When you click the trash icon next to a question, the question will be removed.
  This removal will persist in the database and when you refresh the page. 
  '''
  @app.route('/questions/<int:question_id>', methods=['DELETE'])
  def delete_question(question_id):
    if (not question_id):
      abort(422)
    question = Question.query.get(question_id)
    if (not question):
      abort(404)
    question.delete()
    return jsonify({
      'success': True,
      'deleted': question_id
    })
  '''
  @TODO: 
  Create an endpoint to POST a new question, 
  which will require the question and answer text, 
  category, and difficulty score.

  TEST: When you submit a question on the "Add" tab, 
  the form will clear and the question will appear at the end of the last page
  of the questions list in the "List" tab.  
  '''
  @app.route('/questions', methods=['POST'])
  def add_question():
    body = request.get_json()
    new_question = Question(
      question = body['question'],
      answer = body['answer'],
      category = body['category'],
      difficulty = body['difficulty']
    )
    try:
      new_question.insert()
      return ({
          'success': True,
          'created': new_question.format()
      })
    except:
      abort(422)
  '''
  @TODO: 
  Create a POST endpoint to get questions based on a search term. 
  It should return any questions for whom the search term 
  is a substring of the question. 

  TEST: Search by any phrase. The questions list will update to include 
  only question that include that string within their question. 
  Try using the word "title" to start. 
  '''
  @app.route('/questions/search', methods=['POST'])
  def search_questions():
    body = request.get_json()
    search_term = body['searchTerm']
    if (not search_term):
      abort(422)
    questions = Question.query.filter(Question.question.ilike('%' + search_term + '%')).all()
    formattedQuestions = [question.format() for question in questions]
    if (len(formattedQuestions) == 0):
      abort(404)
    return jsonify({
      'success': True,
      'questions': formattedQuestions,
      'total_questions': len(questions),
    })
  '''
  @TODO: 
  Create a GET endpoint to get questions based on category. 

  TEST: In the "List" tab / main screen, clicking on one of the 
  categories in the left column will cause only questions of that 
  category to be shown. 
  '''
  @app.route('/categories/<int:category_id>/questions', methods=['GET'])
  def category_questions(category_id):
    category_id = category_id + 1
    categories = Category.query.filter(Category.id == category_id).all()
    if (not categories):
      abort(404)
    questions = Question.query.filter(Question.category == category_id).all()
    formattedQuestions = [question.format() for question in questions]
    return jsonify({
      'success': True,
      'questions': formattedQuestions,
      'total_questions': len(questions),
      'current_category': category_id
    })
  '''
  @TODO: 
  Create a POST endpoint to get questions to play the quiz. 
  This endpoint should take category and previous question parameters 
  and return a random questions within the given category, 
  if provided, and that is not one of the previous questions. 

  TEST: In the "Play" tab, after a user selects "All" or a category,
  one question at a time is displayed, the user is allowed to answer
  and shown whether they were correct or not. 
  '''
  @app.route('/quizzes', methods=['POST'])
  def get_quiz():
    try:
      body = request.get_json()
      previous = body['previous_questions']
      quiz_category = body.get('quiz_category', None)
      if quiz_category is None or quiz_category['id'] == 0:
          questions = Question.query.filter(~Question.id.in_(previous)).all()
      else:
          questions = Question.query.filter(Question.category == quiz_category['id'], ~Question.id.in_(previous)).all()
      question = None if len(questions) == 0 else random.choice(questions).format()
      return jsonify({
          'success': True,
          'question': question
      })
    except:
      abort(422)
    finally:
      db.session.close()
  '''
  @TODO: 
  Create error handlers for all expected errors 
  including 404 and 422. 
  '''
  @app.errorhandler(400)
  def bad_request(error):
    return jsonify({
      'success': False,
      'error': 400,
      'message': 'Bad Request'
    }), 400

  @app.errorhandler(404)
  def not_found_error(error):
    return jsonify({
      'success': False,
      'error': 404,
      'message': 'Not Found'
    }), 404

  @app.errorhandler(422)
  def unprocessable_entity(error):
    return jsonify({
      'success': False,
      'error': 422,
      'message': 'Unprocessable Entity'
    }), 422

  @app.errorhandler(500)
  def internal_server_error(error):
    return jsonify({
      'success': False,
      'error': 500,
      'message': 'Internal Server Error'
    }), 500
  
  return app

    