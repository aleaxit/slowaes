# SlowAES #

Implementations of AES in pure scripting languages (currently !Javascript, Python, Ruby, and PHP, but, in addition to further contributions in those languages, submissions in other scripting languages are also entirely welcome!).

Such implementations will be slow (hence the project name) but still useful when faster ones are not available (for example, for JavaScript clients in browsers, and Python servers on Google App Engine).

This code was originally developed by Josh Davis in 2007 and consisted of a mostly working JavaScript implementation (given the name ecmaScrypt) and a quite broken Python implementation. While working on a Google App Engine project Alex Martelli needed a Python AES implementation to do MS Live authentication and stumbled upon Josh's code. Together they decided to start this project, and other committers joined later to supply implementations in other scripting languages.