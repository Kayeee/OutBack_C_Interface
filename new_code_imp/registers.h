/**

40673	466	:	GS_Single_Buy_kW                   	0.1 kW	grid power
40676	469	:	GS_Single_Load_kW                  	0.0 kW	output power
40639	432	:	GS_Single_Inverter_Buy_Current     	0	grid current
40647	440	:	GS_Single_Battery_Voltage          	49.6 V	grid voltage
40643	436	:	GS_Single_AC_Output_Voltage        	0 V	output voltage
40637	430	:	GS_Single_Inverter_Output_Current  	0	output current
40554	337	:	I_Temp_Sink      	20 deg C	internal temp
40536	320	:	I_AC_Frequency   	0.0 Hz	frequency (output?)
40659	452	:	GS_Single_AC_Input_Frequency       	0.0 cycles	grid frequency
40549	332	:	I_DC_Voltage     	49.6 V	input voltage
40547	330	:	I_DC_Current     	Not implemented	input current 
40551	334	:	I_DC_Power       	Not implemented	

**/


// Blocks 
#define SUNSPEC_COMMON_MODEL_BLOCK 0
#define OUTBACK_BLOCK 1
#define OUTBACK_SYSTEM_CONTROL 2
#define SINGLE_PHASE_INVERTER 3
#define OUTBACK_OPTICS_PACKET 4
#define OUTBACK_RADIAN_SINGLE_PHASE_INVERTER 5
#define OUTBACK_RADIAN_INVERTER_CONFIGURATION 6
#define OUTBACK_FLEXNET_DC_BATTERY_MONITOR 7
#define OUTBACK_FLEXNET_DC_BATTERY_MONITOR_CONFIGURATION 8

//Fields
#define GRID_CURRENT_FIELD 432
#define GRID_VOLTAGE_FIELD 440
#define GRID_POWER_FIELD 466
#define OUTPUT_POWER_FIELD 469
#define OUTPUT_VOLTAGE_FIELD 436
#define OUTPUT_CURRENT_FIELD 430
#define INPUT_POWER_FIELD 334
#define INPUT_VOLTAGE_FIELD 332
#define INPUT_CURRENT_FIELD 330
#define INTERNAL_TEMP_FIELD 337
#define AC_FREQUENCY_FIELD 320
#define AC_INPUT_FREQUENCY_FIELD 452
#define VERSION_FIELD 6
#define SN_FIELD 7


struct multiple_register {
	int field; 
	int block;
	char* str;
};

struct multiple_register grid_register [] = {
	
	{GRID_POWER_FIELD,OUTBACK_RADIAN_SINGLE_PHASE_INVERTER, BATT_POWER_STR},
	{GRID_CURRENT_FIELD, OUTBACK_RADIAN_SINGLE_PHASE_INVERTER,BATT_CURR_STR},
	{GRID_VOLTAGE_FIELD, OUTBACK_RADIAN_SINGLE_PHASE_INVERTER, BATT_VOLT_STR},
	
};


struct multiple_register AC_register [] = {
	
	{OUTPUT_POWER_FIELD,OUTBACK_RADIAN_SINGLE_PHASE_INVERTER, AC_POWER_STR},
	{AC_FREQUENCY_FIELD, OUTBACK_RADIAN_SINGLE_PHASE_INVERTER,AC_FREQUENCY_STR},
	{OUTPUT_VOLTAGE_FIELD, OUTBACK_RADIAN_SINGLE_PHASE_INVERTER,AC_VOLTAGE_STR},
	{OUTPUT_CURRENT_FIELD, OUTBACK_RADIAN_SINGLE_PHASE_INVERTER, AC_CURRENT_STR},
	
};


struct multiple_register DC_register [] = {
	
	{INPUT_VOLTAGE_FIELD,SINGLE_PHASE_INVERTER, DC_VOLTAGE_STR},
	{INPUT_CURRENT_FIELD, SINGLE_PHASE_INVERTER,DC_CURRENT_STR},
	{INPUT_POWER_FIELD, SINGLE_PHASE_INVERTER, DC_POWER_STR},
	
};

struct multiple_register reg_all[] = {
	
	{VERSION_FIELD,SUNSPEC_COMMON_MODEL_BLOCK,TEMP_SINK_STR},
	{INPUT_VOLTAGE_FIELD,SINGLE_PHASE_INVERTER, DC_VOLTAGE_STR},
	{INPUT_CURRENT_FIELD, SINGLE_PHASE_INVERTER,DC_CURRENT_STR},
	{INPUT_POWER_FIELD, SINGLE_PHASE_INVERTER, DC_POWER_STR},
	{OUTPUT_POWER_FIELD,OUTBACK_RADIAN_SINGLE_PHASE_INVERTER, AC_POWER_STR},
	{AC_FREQUENCY_FIELD, OUTBACK_RADIAN_SINGLE_PHASE_INVERTER,AC_FREQUENCY_STR},
	{OUTPUT_VOLTAGE_FIELD, OUTBACK_RADIAN_SINGLE_PHASE_INVERTER,AC_VOLTAGE_STR},
	{OUTPUT_CURRENT_FIELD, OUTBACK_RADIAN_SINGLE_PHASE_INVERTER, AC_CURRENT_STR},
	{GRID_POWER_FIELD,OUTBACK_RADIAN_SINGLE_PHASE_INVERTER, BATT_POWER_STR},
	{GRID_CURRENT_FIELD, OUTBACK_RADIAN_SINGLE_PHASE_INVERTER,BATT_CURR_STR},
	{GRID_VOLTAGE_FIELD, OUTBACK_RADIAN_SINGLE_PHASE_INVERTER, BATT_VOLT_STR},
	{VERSION_FIELD,SUNSPEC_COMMON_MODEL_BLOCK,"Firmware"},
	{SN_FIELD,SUNSPEC_COMMON_MODEL_BLOCK,SER_NUM_STR}
};



