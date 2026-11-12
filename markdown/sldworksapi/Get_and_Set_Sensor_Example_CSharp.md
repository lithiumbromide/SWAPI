---
title: "Get and Set Sensor Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_and_Set_Sensor_Example_CSharp.htm"
---

# Get and Set Sensor Example (C#)

This example shows how to get a Measurement (dimension) sensor, resets its value to set off an alert, and fire notifications before resetting value.

```vb
//-------------------------------------------------------------------
 // Preconditions:
 // 1. Open a part document that has a dimension
 /     of 2.5 inches and a corresponding Measurement
 //    (dimension) sensor that has an alert set to
 //    go off if the value of the dimension is
 //    reset to > 3 inches.
 // 2. Select the Measurement (dimension) sensor
 //    of 2.5 inches in the Sensors folder in the
 //    FeatureManager design tree.
 // 3. Open the Immediate window.
 //
 // Postconditions:
 // 1. Enables the Measurement (dimension) sensor alert, if it
 //    wasn't previously enabled.
 // 2. Sets the value of the dimension to 3.5 inches.
 // 3. Triggers the Measurement (dimension) sensor alert; click
 //    OK to close it.
 // 4. Fires an event when updating the dimension; click
 //    OK to close it.
 // 5. Examine the FeatureManager design tree, Immediate window,
 //    and the graphics area.
 //--------------------------------------------------------------------
 using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;
using System.Diagnostics;
using System.Windows.Forms;
using System.Collections;
namespace SensorsCSharp.csproj
{
    partial class SolidWorksMacro
    {
        public PartDoc swPart;
        public void Main()
        {
            ModelDoc2 swModel;
            SelectionMgr swSelMgr;
            Feature swFeat;
            Sensor swSensor;
            DimensionSensorData swDimSensor;
            DisplayDimension swDisplayDim;
            Dimension swDim;
            double alertValue1;
            double alertvalue2;
            double sensorValue;
            int retVal;
            bool retBool;

            Hashtable OpenPart;

            swModel = (ModelDoc2)swApp.ActiveDoc;
            swSelMgr = (SelectionMgr)swModel.SelectionManager;

            //Set up event and attach to it
            swPart = (PartDoc)swModel;
            OpenPart = new Hashtable();
            AttachEventHandlers();

            // Get the selected Measurement (dimension) sensor
            // in the Sensors folder in the FeatureManager
            // design tree
            swFeat = (Feature)swSelMgr.GetSelectedObject6(1, -1);
            swSensor = (Sensor)swFeat.GetSpecificFeature2();

            // Get name of sensor
            Debug.Print("Sensor name = " + swFeat.Name);

            // Make sure selected sensor is a Measurement
            // (dimension) sensor (as of SOLIDWORKS 2009 SP2,
            // only Measurement (dimension) sensors are supported);
            // if it's not, then exit the macro
            if (swSensor == null)
            {
                Debug.Print("Selected sensor is not a Measurement (dimension) sensor. Exiting macro.");
                return;
            }
            // Get type of sensor
            switch (swSensor.SensorType)
            {
                case (int)swSensorType_e.swSensorSimulation:
                    Debug.Print("Sensor type = Simulation");
                    break;
                case (int)swSensorType_e.swSensorMassProperty:
                    Debug.Print("Sensor type = Mass Property");
                    break;
                case (int)swSensorType_e.swSensorDimension:
                    Debug.Print("Sensor type = Measurement (dimension)");
                    break;
                case (int)swSensorType_e.swSensorInterfaceDetection:
                    Debug.Print("Sensor type = Interference Detection");
                    break;
            }

            // Get whether sensor is in an alerted state
            Debug.Print("Is an alert currently triggered for this sensor? " + swSensor.SensorAlertState);

            //Enable sensor's alert
            swSensor.SensorAlertEnabled = true;
            Debug.Print ("Is an alert enabled for this sensor? " + swSensor.SensorAlertEnabled);

            // Get sensor's alert state
            if (swSensor.SensorAlertState)
            {
                switch (swSensor.SensorAlertType)
                {
                    case (int)swSensorAlertType_e.swSensorAlert_GreaterThan:
                        Debug.Print("Sensor alert type = Greater than");
                        break;
                    case (int)swSensorAlertType_e.swSensorAlert_LessThan:
                        Debug.Print("Sensor alert type = Less than");
                        break;
                    case (int)swSensorAlertType_e.swSensorAlert_Exactly:
                        Debug.Print("Sensor alert type = Exactly");
                        break;
                    case (int)swSensorAlertType_e.swSensorAlert_NotGreaterThan:
                        Debug.Print("Sensor alert type = Not greater than");
                        break;
                    case (int)swSensorAlertType_e.swSensorAlert_NotLessThan:
                        Debug.Print("Sensor alert type = Not less than");
                        break;
                    case (int)swSensorAlertType_e.swSensorAlert_NotExactly:
                        Debug.Print("Sensor alert type = Not exactly");
                        break;
                    case (int)swSensorAlertType_e.swSensorAlert_Between:
                        Debug.Print("Sensor alert type = Between");
                        break;
                    case (int)swSensorAlertType_e.swSensorAlert_NotBetween:
                        Debug.Print("Sensor alert type = Not between");
                        break;
                    case (int)swSensorAlertType_e.swSensorAlert_True:
                        Debug.Print("Sensor alert type = True");
                        break;
                    case (int)swSensorAlertType_e.swSensorAlert_False:
                        Debug.Print("Sensor alert type = False");
                        break;
                }
                // Get sensor's alert values
                alertValue1 = swSensor.SensorAlertValue1;
                // ISensor::SensorAlertValue2 only valid when sensor
                // alert type is swSensorAlertType_e.swSensorAlert_Between
                alertvalue2 = swSensor.SensorAlertValue2;
                Debug.Print(" Alert value 1 = " + alertValue1);
                Debug.Print(" Alert value 2 = " + alertvalue2);
            }
            // Set sensor to a different sensor type
            swSensor.SensorType = (int)swSensorType_e.swSensorSimulation;
            switch (swSensor.SensorType)
            {
                case (int)swSensorType_e.swSensorSimulation:
                    Debug.Print("Set sensor type to = Simulation");
                    break;
                case (int)swSensorType_e.swSensorMassProperty:
                    Debug.Print("Set sensor type to = Mass Property");
                    break;
                case (int)swSensorType_e.swSensorDimension:
                    Debug.Print("Set sensor type to = Measurement (dimension)");
                    break;
                case (int)swSensorType_e.swSensorInterfaceDetection:
                    Debug.Print("Set sensor type to = Interference Detection");
                    break;
            }
            // Update and evaluate sensor
            retBool = swSensor.UpdateSensor();

            // Print updated sensor type
            switch (swSensor.SensorType)
            {
                case (int)swSensorType_e.swSensorSimulation:
                    Debug.Print("Sensor updated to type = Simulation");
                    break;
                case (int)swSensorType_e.swSensorMassProperty:
                    Debug.Print("Sensor updated to type = Mass Property");
                    break;
                case (int)swSensorType_e.swSensorDimension:
                    Debug.Print("Sensor updated to type = Measurement (dimension)");
                    break;
                case (int)swSensorType_e.swSensorInterfaceDetection:
                    Debug.Print("Sensor updated to type = Interference Detection");
                    break;
            }
            // Set sensor type back to original type
            swSensor.SensorType = (int)swSensorType_e.swSensorDimension;
            // Update and evaluate sensor again
            retBool = swSensor.UpdateSensor();
            // Print updated sensor type
            switch (swSensor.SensorType)
            {
                case (int)swSensorType_e.swSensorSimulation:
                    Debug.Print("Sensor updated back to type = Simulation");
                    break;
                case (int)swSensorType_e.swSensorMassProperty:
                    Debug.Print("Sensor updated back to type = Mass Property");
                    break;
                case (int)swSensorType_e.swSensorDimension:
                    Debug.Print("Sensor updated back to type = Measurement (dimension)");
                    break;
                case (int)swSensorType_e.swSensorInterfaceDetection:
                    Debug.Print("Sensor updated back to type = Interference Detection");
                    break;
            }
            // Because sensor is a Measurement (dimension) sensor,
            // get the sensor's feature data, object, configuration name, and value
            if (swSensor is DimensionSensorData)
            {
                swDimSensor = (DimensionSensorData)swSensor.GetSensorFeatureData();
                swDisplayDim = (DisplayDimension)swDimSensor.GetDisplayDimension();
                // Get Measurement (dimension) sensor value
                sensorValue = swDimSensor.SensorValue;
                // Convert meters to inches
                Debug.Print("Sensor value: " + (sensorValue * 39.37) + " inches");
                // Get the actual dimension and update
                // to a value that sets off the alert
                swDim = (Dimension)swDisplayDim.GetDimension2(1);
                // Reset and update the Measurement (dimension) to 3.5 inhces
                retVal = swDim.SetValue3(3.5, (int)swSetValueInConfiguration_e.swSetValue_UseCurrentSetting, "Configuration");
                retBool = swSensor.UpdateSensor();
                swModel.ForceRebuild3(true);
                // Get Measurement (dimension) sensor value again
                sensorValue = swDimSensor.SensorValue;
                Debug.Print("New sensor value: " + (sensorValue * 39.37) + " inches");
            }
        }
        /// <summary>
        /// The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
        //Attach to and fire event
        public void AttachEventHandlers()
        {
            AttachSWEvents();
        }
        public void AttachSWEvents()
        {
            swPart.SensorAlertPreNotify += this.swPart_SensorAlertPreNotify;
        }
        public int swPart_SensorAlertPreNotify(object SensorIn, int SensorAlertType)
        {
            MessageBox.Show("The value of the sensor deviates from its limits.");
            return 1;
        }
    }

}
```
