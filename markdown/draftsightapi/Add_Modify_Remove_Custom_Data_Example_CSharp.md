---
title: "Add, Modify, and Remove Custom Data Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Add_Modify_Remove_Custom_Data_Example_CSharp.htm"
---

# Add, Modify, and Remove Custom Data Example (C#)

This example shows how to add, modify, and remove custom data from a Circle.

```
//--------------------------------------------------------------
//Preconditions:
// 1. Create a C# Windows console project.
// 2. Copy and paste this example into the C# IDE.
// 3. Add a reference to:
//    install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.dll
// 4. Add references to System and System.Windows.Forms.
// 5. Open the Immediate window.
// 6. Start DraftSight and open a document.
// 7. Click Start Debugging.
//
//Postconditions:
// 1. Circle is constructed.
// 2. Custom data is added to, modified, and removed from
//    the Circle.
// 3. Examine the Immediate window to verify.
//----------------------------------------------------------------
using System;
using System.Runtime.InteropServices;
using System.Windows.Forms;
using System.Diagnostics;
using DraftSight.Interop.dsAutomation;
```

```
namespace SetAndGetXData
{
    class Program
    {
        private static DraftSight.Interop.dsAutomation.Application dsApp;
```

```
        static void Main(string[] args)
        {
            //Connect to DraftSight application
            dsApp = (DraftSight.Interop.dsAutomation.Application)Marshal.GetActiveObject("DraftSight.Application");
            dsApp.AbortRunningCommand(); // abort any command currently running in DraftSight to avoid nested commands
```

```
            //Get active document
            Document dsDoc = dsApp.GetActiveDocument();
            if (null == dsDoc)
            {
                MessageBox.Show("There are no open documents in DraftSight.");
                return;
            }
```

```
            //Get model space
            Model dsModel = dsDoc.GetModel();
```

```
            //Get sketch manager
            SketchManager dsSketchMgr = dsModel.GetSketchManager();
```

```
            //Draw a Circle
            double centerX = 1, centerY = 1, centerZ = 0;
            double radius = 5;
            Circle dsCircle = dsSketchMgr.InsertCircle(centerX, centerY, centerZ, radius);
```

```
            //Zoom to fit
            dsApp.Zoom(dsZoomRange_e.dsZoomRange_Fit, null, null);
```

```
            //Add custom data to the Circle
            string applicationName = "CircleApp";
            AddCustomDataToCircle(dsCircle, applicationName);
```

```
            Debug.Print(Environment.NewLine + "Circle custom data..." + Environment.NewLine);
```

```
            //Print custom data
            PrintCustomDataInfo(dsCircle.GetCustomData(applicationName));
```

```
            //Change custom data
            CustomData dsCustomData = dsCircle.GetCustomData(applicationName);
            ChangeCustomData(dsCustomData);
```

```
            //Apply the changed custom data to the Circle
            dsCircle.SetCustomData(applicationName, dsCustomData);
```

```
            Debug.Print(Environment.NewLine + "Custom data changed..." + Environment.NewLine);
```

```
            //Print custom data after changing it
            PrintCustomDataInfo(dsCircle.GetCustomData(applicationName));
```

```
            //Remove all string values from custom data
            dsCustomData = dsCircle.GetCustomData(applicationName);
            DeleteStringDataFromCustomData(dsCustomData, dsCustomDataType_e.dsCustomDataType_String);
```

```
            //Apply the changed custom data to the Circle
            dsCircle.SetCustomData(applicationName, dsCustomData);
```

```
            Debug.Print(Environment.NewLine + "Removed all string values from custom data..." + Environment.NewLine);
```

```
            //Print custom data after removing elements
            PrintCustomDataInfo(dsCircle.GetCustomData(applicationName));
```

```
            //Delete custom data from the Circle
            dsCircle.DeleteCustomData(applicationName);
```

```
            Debug.Print(Environment.NewLine + "The custom data for the circle is removed..." + Environment.NewLine);
```

```
            //Print custom data after removing it from the Circle
            PrintCustomDataInfo(dsCircle.GetCustomData(applicationName));
```

```
        }
```

```
        private static void AddCustomDataToCircle(Circle dsCircle, string applicationName)
        {
            //Get custom data for the Circle
            CustomData dsCustomData = dsCircle.GetCustomData(applicationName);
```

```
            //Clear existing custom data
            dsCustomData.Empty();
```

```
            //Get the index
            int index = dsCustomData.GetDataCount();
```

```
            //Add a description of the Circle as a string value to the custom data
            int markerForString = 1000;
            dsCustomData.InsertStringData(index, markerForString, "Circle entity");
```

```
            //Get the next index
            index = dsCustomData.GetDataCount();
```

```
            //Add custom data section to custom data
            CustomData dsInnerCustomData = dsCustomData.InsertCustomData(index);
```

```
            //Get the next index
            index = dsInnerCustomData.GetDataCount();
```

```
            //Get the center point of the Circle
            //and add it as point data to the custom data
            int markerForPoint = 1011;
            double centerX, centerY, centerZ;
            dsCircle.GetCenter(out centerX, out centerY, out centerZ);
            dsInnerCustomData.InsertPointData(index, markerForPoint, centerX, centerY, centerZ);
```

```
            //Get the next index
            index = dsInnerCustomData.GetDataCount();
```

```
            //Get the radius of the Circle
            //and add it as double data to the custom data
            int markerForDouble = 1040;
            double doubleValue = dsCircle.Radius;
            dsInnerCustomData.InsertDoubleData(index, markerForDouble, doubleValue);
```

```
            //Get the next index
            index = dsInnerCustomData.GetDataCount();
```

```
            //Add the layer name of Circle as layer name data
            //to custom data
            dsInnerCustomData.InsertLayerName(index, dsCircle.Layer);
```

```
            //Get the next index
            index = dsInnerCustomData.GetDataCount();
```

```
            //Add the name of the LineStyle of the Circle
            //as a string data to custom data
            dsInnerCustomData.InsertStringData(index, markerForString, dsCircle.LineStyle);
```

```
            //Get the next index
            index = dsInnerCustomData.GetDataCount();
```

```
            //Add Int16 data to custom data
            int markerForInt16 = 1070;
            Int16 intValue = 5;
            dsInnerCustomData.InsertInteger16Data(index, markerForInt16, intValue);
```

```
            //Get the next index
            index = dsInnerCustomData.GetDataCount();
```

```
            //Add Int32 data to custom data
            int markerForInt32 = 1071;
            Int32 int32Value = 7;
            dsInnerCustomData.InsertInteger32Data(index, markerForInt32, int32Value);
```

```
            //Get the next index
            index = dsInnerCustomData.GetDataCount();
```

```
            //Add the handle of the Circle as handle data to custom data
            dsInnerCustomData.InsertHandle(index, dsCircle.Handle);
```

```
            //Get the next index
            index = dsInnerCustomData.GetDataCount();
```

```
            //Add binary data to custom data
            byte[] binaryDataArray = new byte[] { 0, 1, 0, 1 };
            dsInnerCustomData.InsertByteData(index, binaryDataArray);
```

```
            //Set custom data
            dsCircle.SetCustomData(applicationName, dsCustomData);
        }
```

```
        private static void DeleteStringDataFromCustomData(CustomData dsCustomData, dsCustomDataType_e dataType)
        {
            //Get custom data count
            int count = dsCustomData.GetDataCount();
```

```
            for (int index = count - 1; index >= 0; --index)
            {
                //Get custom data type
                dsCustomDataType_e customDataType;
                dsCustomData.GetDataType(index, out customDataType);
```

```
                if (customDataType == dataType)
                {
                    //Delete custom data element
                    dsCustomData.Delete(index);
                }
```

```
                if (customDataType == dsCustomDataType_e.dsCustomDataType_CustomData)
                {
                    //Get inner custom data
                    CustomData dsInnerCustomData;
                    dsCustomData.GetCustomData(index, out dsInnerCustomData);
```

```
                    DeleteStringDataFromCustomData(dsInnerCustomData, dataType);
                }
            }
        }
```

```
        private static void ChangeCustomData(CustomData dsCustomData)
        {
            //Get custom data count
            int count = dsCustomData.GetDataCount();
```

```
            for (int index = 0; index < count; ++index)
            {
                //Get custom data type
                dsCustomDataType_e dataType;
                dsCustomData.GetDataType(index, out dataType);
```

```
                switch (dataType)
                {
                    case dsCustomDataType_e.dsCustomDataType_BinaryData:
                        {
                            //Get binary data from custom data
                            byte[] binaryDataArray = (byte[])dsCustomData.GetByteData(index);
```

```
                            //Check if binary data is not empty
                            if (null != binaryDataArray)
                            {
                                for (int i = 0; i < binaryDataArray.Length; ++i)
                                {
                                    binaryDataArray[i]++;
                                }
```

```
                                //Set the updated binary data to custom data
                                dsCustomData.SetByteData(index, binaryDataArray);
                            }
```

```
                            break;
                        }
                    case dsCustomDataType_e.dsCustomDataType_CustomData:
                        {
                            //Get the inner custom data
                            CustomData dsInnerCustomData;
                            dsCustomData.GetCustomData(index, out dsInnerCustomData);
```

```
                            ChangeCustomData(dsInnerCustomData);
```

```
                            break;
                        }
                    case dsCustomDataType_e.dsCustomDataType_Double:
                        {
                            //Get double custom data
                            double doubleValue;
                            dsCustomData.GetDoubleData(index, out doubleValue);
```

```
                            //Change double value
                            doubleValue += 1;
```

```
                            //Set the updated double value to custom data
                            dsCustomData.SetDoubleData(index, doubleValue);
```

```
                            break;
                        }
                    case dsCustomDataType_e.dsCustomDataType_Integer16:
                        {
                            //Get Int16 custom data
                            int intValue;
                            dsCustomData.GetInteger16Data(index, out intValue);
```

```
                            //Change Int16 value
                            intValue++;
```

```
                            //Set the updated Int16 value to custom data
                            dsCustomData.SetInteger16Data(index, intValue);
```

```
                            break;
                        }
                    case dsCustomDataType_e.dsCustomDataType_Integer32:
                        {
                            //Get Int32 custom data
                            Int32 intValue;
                            dsCustomData.GetInteger32Data(index, out intValue);
```

```
                            //Change Int32 value
                            intValue++;
```

```
                            //Set the updated Int32 value to custom data
                            dsCustomData.SetInteger32Data(index, intValue);
```

```
                            break;
                        }
                    case dsCustomDataType_e.dsCustomDataType_Point:
                        {
                            //Get point custom data
                            double x, y, z;
                            dsCustomData.GetPointData(index, out x, out y, out z);
```

```
                            //Change point coordinates
                            x += 2;
                            y += 2;
                            z += 2;
```

```
                            //Set the updated point coordinates to custom data
                            dsCustomData.SetPointData(index, x, y, z);
```

```
                            break;
                        }
                    case dsCustomDataType_e.dsCustomDataType_String:
                        {
                            //Get string custom data
                            string stringValue;
                            dsCustomData.GetStringData(index, out stringValue);
```

```
                            //Modify string value
                            stringValue += "_Changed";
```

```
                            //Set the updated string value to custom data
                            dsCustomData.SetStringData(index, stringValue);
```

```
                            break;
                        }
                    default:
                        break;
                }
            }
        }
```

```
        private static void PrintCustomDataInfo(CustomData dsCustomData)
        {
            //Get custom data count
            int count = dsCustomData.GetDataCount();
            Debug.Print("Custom data count:" + count.ToString());
```

```
            for (int index = 0; index < count; ++index)
            {
                //Get custom data type
                dsCustomDataType_e dataType;
                dsCustomData.GetDataType(index, out dataType);
```

```
                //Get custom data marker
                int marker;
                dsCustomData.GetDataMarker(index, out marker);
```

```
                switch (dataType)
                {
                    case dsCustomDataType_e.dsCustomDataType_BinaryData:
                        {
                            //Get binary data from custom data
                            byte[] binaryDataArray = (byte[])dsCustomData.GetByteData(index);
                            string binaryDataContent = string.Empty;
```

```
                            if (null == binaryDataArray)
                            {
                                binaryDataContent = "Empty";
                            }
                            else
                            {
                                foreach (byte binaryData in binaryDataArray)
                                {
                                    binaryDataContent += binaryData.ToString() + ",";
                                }
                            }
```

```
                            //Print custom data index, data type, marker, and binary value
                            PrintCustomDataElement(index, dataType, marker, binaryDataContent);
```

```
                            break;
                        }
                    case dsCustomDataType_e.dsCustomDataType_CustomData:
                        {
                            //Get inner custom data
                            CustomData dsGetCustomData;
                            dsCustomData.GetCustomData(index, out dsGetCustomData);
```

```
                            PrintCustomDataInfo(dsGetCustomData);
```

```
                            break;
                        }
                    case dsCustomDataType_e.dsCustomDataType_Double:
                        {
                            //Get double value from custom data
                            double doubleValue;
                            dsCustomData.GetDoubleData(index, out doubleValue);
```

```
                            //Print custom data index, data type, marker and double value
                            PrintCustomDataElement(index, dataType, marker, doubleValue);
```

```
                            break;
                        }
                    case dsCustomDataType_e.dsCustomDataType_Handle:
                        {
                            //Get handle value from custom data
                            string handle = dsCustomData.GetHandleData(index);
```

```
                            //Print custom data index, data type, marker, and handle value
                            PrintCustomDataElement(index, dataType, marker, handle);
```

```
                            break;
                        }
                    case dsCustomDataType_e.dsCustomDataType_Integer16:
                        {
                            int intValue;
                            dsCustomData.GetInteger16Data(index, out intValue);
```

```
                            //Print custom data index, data type, marker, and Int16 value
                            PrintCustomDataElement(index, dataType, marker, intValue);
```

```
                            break;
                        }
                    case dsCustomDataType_e.dsCustomDataType_Integer32:
                        {
                            Int32 intValue;
                            dsCustomData.GetInteger32Data(index, out intValue);
```

```
                            //Print custom data index, data type, marker, and Int32 value
                            PrintCustomDataElement(index, dataType, marker, intValue);
```

```
                            break;
                        }
                    case dsCustomDataType_e.dsCustomDataType_LayerName:
                        {
                            //Get layer name from custom data
                            string layerName;
                            dsCustomData.GetLayerName(index, out layerName);
```

```
                            //Print custom data index, data type, marker, and layer name value
                            PrintCustomDataElement(index, dataType, marker, layerName);
```

```
                            break;
                        }
                    case dsCustomDataType_e.dsCustomDataType_Point:
                        {
                            //Get point coordinates from custom data
                            double x, y, z;
                            dsCustomData.GetPointData(index, out x, out y, out z);
```

```
                            //Print custom data index, data type, marker, and point values
                            string pointCoordinates = x + "," + y + "," + z;
                            PrintCustomDataElement(index, dataType, marker, pointCoordinates);
```

```
                            break;
                        }
                    case dsCustomDataType_e.dsCustomDataType_String:
                        {
                            //Get string value from custom data
                            string stringValue;
                            dsCustomData.GetStringData(index, out stringValue);
```

```
                            //Print custom data index, data type, marker, and string value
                            PrintCustomDataElement(index, dataType, marker, stringValue);
```

```
                            break;
                        }
                    case dsCustomDataType_e.dsCustomDataType_Unknown:
                        {
                            //Print custom data index, data type, marker and value
                            PrintCustomDataElement(index, dataType, marker, "Unknown value");
```

```
                            break;
                        }
                    default:
                        break;
                }
            }
        }
```

```
        private static void PrintCustomDataElement(int index, dsCustomDataType_e dataType, int marker, object customDataValue)
        {
            //Print custom data index, data type, marker and value
            string message = "Index: " + index.ToString();
            message += " Data type: " + dataType.ToString();
            message += " Marker: " + marker.ToString();
            message += " Value: " + customDataValue.ToString();
```

```
            Debug.Print(message);
        }
    }
}
```
