from setuptools import setup, find_packages

setup(
    name='chat_piano',  # Replace with your project name
    version='0.1.0',  # The current project version
    author='Music X Lab',  # Replace with your organization or team name
    author_email='your-email@example.com',  # Replace with your contact email
    description='Chat Piano: Leveraging AI to interpret voice commands and convert them into MIDI files.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yhbcode000/ChatPiano',
    packages=find_packages(include=['modules', 'modules.*']),  # Include submodules explicitly
    include_package_data=True,
    install_requires=[
        'numpy>=1.24.3',
        'torch>=1.10.0',
        'mido>=1.2.10',
        'pydub>=0.25.1',
        'requests>=2.26.0',
        'docker>=5.0.0',
        'PyYAML>=6.0',
    ],
    extras_require={
        'dev': [
            'pytest>=7.0.0',
            'flake8>=4.0.0',
        ],
        'test': [
            'pytest>=7.0.0',
            'coverage>=6.0',
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
    ],
    python_requires='>=3.10',
    entry_points={
        'console_scripts': [
            'start-chatpiano=modules.some_module:main',  # Replace with the actual entry point for your application
        ],
    },
)
