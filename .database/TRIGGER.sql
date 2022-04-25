/* UDPATE CURRENT TANK FUEL BASED ON FILL */
CREATE OR REPLACE FUNCTION CHANGE_CURRENT_TANK_FUEL()
RETURNS trigger AS '
BEGIN
	UPDATE app_tank
    SET "currentFuel" = (app_tank."currentFuel" - new."quantityLiters")
    FROM app_fuelpump
    WHERE new."pump_id" = app_fuelpump."id" AND app_tank."id" = app_fuelpump."tank_id";
RETURN NEW;
END;
'
LANGUAGE plpgsql;


CREATE OR REPLACE TRIGGER FILL_UPP_TRIGGER
AFTER INSERT OR UPDATE ON app_fill
FOR EACH ROW
EXECUTE PROCEDURE CHANGE_CURRENT_TANK_FUEL();