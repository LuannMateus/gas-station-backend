/* TANK LOAD DATA */
INSERT INTO public."app_tank" ("id", "type", "maxCapacity", "currentFuel") VALUES (
   '0a3cad93-a913-4ac7-8de9-569e6fcbce3c',  
   'Gasolina',
    30000,
    30000
);

INSERT INTO public."app_tank" ("id", "type", "maxCapacity", "currentFuel") VALUES (
   'd4f6b05f-d9fd-4fb8-933c-e74dad923d62',  
   'Óleo Diesel',
    30000,
    30000
);

/* FUEL PUMP LOAD DATA */
INSERT INTO public."app_fuelpump" ("id", "type", "pricePerLiter", "tank_id") VALUES (
   '0d4b5a8f-7946-4777-9103-372f1df58c53',  
   'Gasolina A',
    8,
    '0a3cad93-a913-4ac7-8de9-569e6fcbce3c'
);

INSERT INTO public."app_fuelpump" ("id", "type", "pricePerLiter", "tank_id") VALUES (
   'aea801b9-9557-46af-afca-e4233875abf0',  
   'Gasolina B',
    8,
    '0a3cad93-a913-4ac7-8de9-569e6fcbce3c'
);

INSERT INTO public."app_fuelpump" ("id", "type", "pricePerLiter", "tank_id") VALUES (
   '7c0406d7-fc4a-4319-b928-4ac3ac931e1a',  
   'Óleo Diesel A',
    7,
    'd4f6b05f-d9fd-4fb8-933c-e74dad923d62'
);

INSERT INTO public."app_fuelpump" ("id", "type", "pricePerLiter", "tank_id") VALUES (
   '426a515d-5332-4418-948e-04740d64a929',  
   'Óleo Diesel B',
    7,
    'd4f6b05f-d9fd-4fb8-933c-e74dad923d62'
);

/* FILL LOAD DATA 
    * SEGUE A LÓGICA DA APLICAÇÃO
*/
