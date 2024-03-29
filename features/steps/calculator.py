from behave import *
import pdb

@when(u'I go to the tip calculator')
def step_impl(context):
    context.browser.get('http://localhost:5000')

@then(u'I should see the calculator form')
def step_impl(context):
    assert context.browser.title == "Tip calculator"


@when(u'I submit the form with a valid total and tip percentage')
def step_impl(context):
    br = context.browser
    br.get('http://localhost:5000')
    meal_cost = br.find_element_by_name("meal_cost")
    meal_cost.send_keys("30")
    tip_percentage = br.find_element_by_name("tip_percentage")
    tip_percentage.send_keys("20")
    br.find_element_by_id("submit").click()

@then(u'I should see the results page')
def step_impl(context):
    br = context.browser
    assert br.find_element_by_id('results')


@when(u'I submit the form with a $50 total and 20% tip')
def step_impl(context):
    br = context.browser
    br.get('http://localhost:5000')
    meal_cost = br.find_element_by_name("meal_cost")
    meal_cost.send_keys("50")
    tip_percentage = br.find_element_by_name("tip_percentage")
    tip_percentage.send_keys("20")
    br.find_element_by_id("submit").click()

@then(u'I should see a $10 tip amount')
def step_impl(context):
    br = context.browser
    tip = br.find_element_by_id("tip").text
    assert (tip == "Tip = $10.0")


@when(u'I submit the form with a negative {meal_cost} or {tip} amount')
def step_impl(context, meal_cost, tip):
    br = context.browser
    br.get('http://localhost:5000')
    meal_cost = br.find_element_by_name('meal_cost')
    meal_cost.send_keys(meal_cost)
    tip_percentage = br.find_element_by_name('tip_percentage')
    tip_percentage.send_keys(tip)
    br.find_element_by_id("submit").click()

@then(u'I should see a warning')
def step_impl(context):
    br = context.browser
    output = br.find_element_by_id("results").text
    assert output.find('non negative value for the') >= 0

@when(u'I submit the form with a non-number {meal} or {tip} value')
def step_impl(context, meal, tip):
    br = context.browser
    br.get('http://localhost:5000')
    meal_cost = br.find_element_by_name("meal_cost")
    meal_cost.send_keys(meal)
    tip_percentage = br.find_element_by_name("tip_percentage")
    tip_percentage.send_keys(tip)
    br.find_element_by_id("submit").click()

@then(u'I should see an invalid input warning')
def step_impl(context):
    br = context.browser
    output = br.find_element_by_id("results").text
    assert output.find('Invalid data: please enter a number for the') >= 0
