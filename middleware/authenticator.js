module.exports = (req, res, next) => {
    const token = req.get('token');
    if (!token) {
        res.setHeader('WWW-Authenticate', 'Basic realm="SCP"');
        res.status(401).send({
            errors: [{
                status: '401',
                title: 'Unauthorized',
                detail: '"token" header is required'
            }]
        });
        return;
    }
    if(token == "bob"){
      next();
    }
    else {
      res.setHeader('WWW-Authenticate', 'Basic realm="SCP"');
      res.status(402).send({
          errors: [{
              status: '401',
              title: 'Forbidden',
              detail: 'Token mismatch'
          }]
      });
      return;
    }
  }
