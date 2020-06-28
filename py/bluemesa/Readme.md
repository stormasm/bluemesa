Start of top level bluemesa python package.

Key points that will eventually be documented...

All modules that write to redis should be
in either the redis module or the tests module.

Reading from redis is permitted is other modules.

Eventually if I am only using redis for a symboltable
symbol to name function then I could get that out of
a json symbol to name file.

Do not pollute other modules with references to redis,
unless it follows the above rules.
