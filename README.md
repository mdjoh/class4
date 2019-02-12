To build the Docker image in current directory, type in BASH:
docker build -t mdjoh/my-new-image:v01 ./

To show Docker image, type in BASH:
docker images

To run the Docker image, type in BASH:
docker run -t mdjoh/my-new-image:v01

#################################################################

CONTINUOUS INTEGRATION

Continuous integration (CI) is the process of merging relevant files into a repository for development purposes on a regular basis. The advantage of this is that degbugging becomes easier since errors can be detected and dealt with at earlier stages of development rather than later and the amount of back-tracking is reduced. As a result, a solid foundation is built and more time can be spent on developing subsequent components instead of debugging existing code that may compromise incoming code. Frequent committing is how CI would be used on Github.
