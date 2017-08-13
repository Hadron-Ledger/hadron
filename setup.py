from setuptools import setup, find_packages


setup(name='hadronutils',
      install_requires=[
          'werkzeug',
          'gevent>=1.1.0',
          'gunicorn',
          'web3',
          'jinja2',
          'py-solc',
          'pytest',
          'solc'
      ],
      entry_points={
          "console_scripts": [
              "hadron=hadronutils.utils:run_generator",
          ]
      },
      include_package_data=True,
      packages=find_packages(),
      package_data={
          'hadron': [
              'default.conf',
          ],
          # 'hadron.node': [
          #     'static/css/*.css',
          #     'static/images/*.png',
          #     'static/js/*.js',
          #     'templates/*.html',
          # ],
      },
      zip_safe=False)
