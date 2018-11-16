import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="macawspeak",
#    packages=["macaw"],
    version="0.1.0",
    author="Dakota Chambers",
    author_email="dakotachambers@gmail.com",
    description="Better password generation inspired by our colorful, feathered friends.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dcchambers/macaw",
    packages=setuptools.find_packages(),
    keywords = [
		"password",
        "macaw",
	],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points = {
		"console_scripts": [
			"macaw=macaw.macaw:main"
		]
	}
)
