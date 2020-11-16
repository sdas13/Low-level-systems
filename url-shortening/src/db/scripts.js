// Mongodb schema and validations

// use urlshorteningdb;

db.createCollection('URL', {
  validator: {
    $jsonSchema: {
      bsonType: 'object',
      required: ['Hash', 'OriginalURL'],
      properties: {
        Hash: {
          bsonType: 'string',
          description: 'Hash is required and must be a string',
        },
        OriginalURL: {
          bsonType: 'string',
          description: 'OriginalURL is required and must be a string',
        },
        CreationDate: {
          bsonType: 'date',
          description: 'CreationDate must be a date',
        },
        ExpirationDate: {
          bsonType: 'date',
          description: 'ExpirationDate must be a date',
        },
      },
    },
  },
});

db.createCollection('OFFLINE-KEYS', {
  validator: {
    $jsonSchema: {
      bsonType: 'object',
      required: ['Key'],
      properties: {
        Key: {
          bsonType: 'string',
          description: 'Key must be a string',
        },
      },
    },
  },
});
