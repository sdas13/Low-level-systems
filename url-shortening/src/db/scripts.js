// Mongodb schema and validations

use urlshorteningdb;

db.createCollection('URL',{
    validator:{ 
        $jsonSchema : {
            bsonType:"object",
            required : ["Hash", "OriginalURL"],
            properties :{
                Hash : {
                    bsonType:"string",
                    description:"Hash is required and must be a string"
                },
                OriginalURL:{
                    bsonType:"string",
                    description:"OriginalURL is required and must be a string"
                },
                CreationDate:{
                    bsonType:"date",
                    description:"CreationDate must be a date"
                },
                ExpirationDate:{
                    bsonType:"date",
                    description:"ExpirationDate must be a date"
                }
            }
        }

    }
})