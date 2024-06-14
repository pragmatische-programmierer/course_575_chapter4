# Stepik Course 575 Chapter 4
Using Page Object patterns and improving test design.
Browser driver by default: chrome.
1. Run only review tests
pytest -v --tb=line --language=en -m need_review
2. After review please exclude test step13.
Uncomment #@pytest.mark.skip(reason="Uncomment this mark if you don't need run test from Chapter 4 Lesson 3 Step 13")
3. Run specific tests with more output info:
pytest -s --language=en -m step2 test_product_page.py
pytest -s --language=ru -m step3 test_product_page.py
pytest -s --language=es -m step4 test_product_page.py
pytest -s --language=es -m step6 test_product_page.py
pytest -s --language=de -m step8 test_product_page.py
pytest -s --language=it -m step8 test_product_page.py
4. Run all tests for product_page.
With more output:
pytest -s --language=en test_product_page.py
or short info:
pytest -v --tb=line --language=en test_product_page.py
 

