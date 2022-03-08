db = db.getSiblingDB("pirates-api");

db.createUser({
  user: 'root',
  pwd: '12345',
  roles: [{role: 'readWrite', db: 'piratas-api'}]
});