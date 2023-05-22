from setuptools import setup, find_packages
setup(name="test-framework",
      version="0.11",
      url="https://github.com/realdeal87/Opencart-Testing-Project",
      license="GPL",
      author="realdeal87",
      author_email="realdeal87@protonmail.com",
      description="Opencart-Testing-Project",
      packages=["01_basic_test", "02_search_elements", "02_search_elements/locators",
                "03_PageObject/locators", "03_PageObject/pageobjects",
                "03_PageObject/pageobjects/common", "04_statistics/"],
      long_description=open('README.md').read(),
      setup_requires=["pytest==4.6.0", "requests==2.31.0", "ipython", "selenium",
                      "pylint", "browsermob-proxy", "allure-pytest==2.7.0",
                      "psutil", "pymysql", "paramiko"],
      zip_safe=False)
