---
title: "Add and Delete Appearances from Specific Display States Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Add_and_Delete_Materials_from_Specific_Display_States_Example_CSharp.htm"
---

# Add and Delete Appearances from Specific Display States Example (C#)

This example shows how to add an appearance to and delete an appearance from specific display states.

```vb
 //---------------------------------------------------------------------------
// Preconditions:
// 1. Specified model exists.
// 2. Specified appearance exists.
// 3. Open an Immediate window.
//
// Postconditions:
// 1. Creates Display State 2 and Display State 3 for the active
//    configuration.
// 2. Applies specified appearance to all display states of the active
//    configuration.
// 3. Press F5.
// 4. Deletes specified appearance from all display states of the active
//    configuration.
// 5. Press F5.
// 6. Closes document.
 //---------------------------------------------------------------------------
```

```vb
using
```

Microsoft.VisualBasic;

```vb
using
```

System;

```vb
using
```

System.Collections;

```vb
using
```

System.Collections.Generic;

```vb
using
```

System.Data;

```vb
using
```

System.Diagnostics;

```vb
using
```

SolidWorks.Interop.sldworks;

```vb
using
```

SolidWorks.Interop.swconst;

```vb
using
```

System.Runtime.InteropServices;

```vb
namespace
```

RenderMaterials_CSharp.csproj

```vb
{
```

partial class SolidWorksMacro

```vb
    {
```

ModelDoc2

swModel;

Configuration

swConfig;

ModelDocExtension

swModelDocExt;

Entity

swEntity;

SelectionMgr

swSelMgr;

RenderMaterial

swRenderMaterial;

object

[] displayStateNames;

bool

status;

string

modelName;

string

materialName;

int

errors;

int

warnings;

int

nbrDisplayStates;

int

i;

int

k;

int

nbrMaterials;

int

materialID1;

int

materialID2;

int[] materialID1_ToDelete = new int

[1];

int[] materialID2_ToDelete = new int

[1];

public void

Main()

```vb
{
```

```vb
modelName =
```

"C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\dimxpert\\bracket_auto_manual.sldprt"

;

```vb
swModel = swApp.OpenDoc6(modelName, (
```

int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref

warnings);

```vb
swModelDocExt = swModel.Extension;
```

// Get active configuration and create a new display

// state for this configuration

```vb
swConfig = (
```

Configuration

)swModel.**GetActiveConfiguration**();

```vb
status = swConfig.CreateDisplayState(
```

"Display State 2"

);

```vb
swModel.ForceRebuild3(
```

true

);

// Get active configuration and create another new

// display state for this configuration

```vb
swConfig = (
```

Configuration

)swModel.**GetActiveConfiguration**();

```vb
status = swConfig.CreateDisplayState(
```

"Display State 3"

);

```vb
swModel.ForceRebuild3(
```

true

);

// Create appearance

```vb
materialName =
```

"C:\\Program Files\\SolidWorks Corp\\SolidWorks\\data\\graphics\\materials\\metal\\steel\\stainless steel treadplate.p2m"

;

```vb
swRenderMaterial = swModelDocExt.CreateRenderMaterial(materialName);
```

// Select a face and add the appearance to that face

```vb
status = swModelDocExt.SelectByID2(
```

"", "FACE", 0.07151920610502, 0.0952597996959, 0.009524999999996, false, 0, null

, 0);

```vb
swSelMgr = (
```

SelectionMgr

)swModel.**SelectionManager**;

```vb
swEntity = (
```

Entity

)swSelMgr.**GetSelectedObject6**(1, -1);

```vb
status = swRenderMaterial.AddEntity(swEntity);
```

// Get the names of display states

```vb
displayStateNames = (
```

object

[])swConfig.**GetDisplayStates**();

```vb
nbrDisplayStates = swConfig.GetDisplayStatesCount();
```

Debug.Print("This configuration's display states ="

);

for

(i = 0; i <= (nbrDisplayStates - 1); i++)

```vb
{
```

Debug.Print(" Display state name = "

+ displayStateNames[i]);

```vb
}
```

// Add appearance to all of the display states

```vb
status = swModelDocExt.AddDisplayStateSpecificRenderMaterial(swRenderMaterial, (
```

int)swDisplayStateOpts_e.swAllDisplayState, displayStateNames, out materialID1, out

materialID2);

// Get the appearance IDs and names

```vb
swRenderMaterial.GetMaterialIds(
```

out materialID1, out

materialID2);

Debug.Print(" Appearance IDs:"

);

Debug.Print(" ID1 = "

+ materialID1);

Debug.Print(" ID2 = "

+ materialID2);

```vb
nbrMaterials = swModelDocExt.GetRenderMaterialsCount2((
```

int)swDisplayStateOpts_e.swAllDisplayState, null

);

Debug.Print(" Number of materials: "

+ nbrMaterials);

for

(k = 0; k <= (nbrMaterials - 1); k++)

```vb
{
```

Debug.Print(" Name of appearance " + (k + 1) + ": "

+ swModel.**MaterialIdName**);

```vb
}
```

double

xcoord = 0;

double

ycoord = 0;

double

zcoord = 0;

```vb
swRenderMaterial.GetCenterPoint2(
```

out xcoord, out ycoord, out

zcoord);

Debug.Print(""

);

Debug.Print("Texture-based appearance data:"

);

Debug.Print("X coordinate of center point: "

+ xcoord);

Debug.Print("Y coordinate of center point: "

+ ycoord);

Debug.Print("Z coordinate of center point: "

+ zcoord);

```vb
swRenderMaterial.GetUDirection2(
```

out xcoord, out ycoord, out

zcoord);

Debug.Print("X coordinate of U direction: "

+ xcoord);

Debug.Print("Y coordinate of U direction: "

+ ycoord);

Debug.Print("Z coordinate of U direction: "

+ zcoord);

```vb
swRenderMaterial.GetVDirection2(
```

out xcoord, out ycoord, out

zcoord);

Debug.Print("X coordinate of V direction: "

+ xcoord);

Debug.Print("Y coordinate of V direction: "

+ ycoord);

Debug.Print("Z coordinate of V direction: "

+ zcoord);

Debug.Print(""

);

```vb
swModel.ClearSelection2(
```

true

);

```vb
swModel.ForceRebuild3(
```

true

);

Debug.Print("Model has an appearance: "

+ swModelDocExt.**HasMaterialPropertyValues**());

object dispStates = null

;

```vb
status = swRenderMaterial.SetLinkedDisplayStates((
```

int)swDisplayStateOpts_e

.swAllDisplayState, displayStateNames);

```vb
dispStates = swRenderMaterial.GetLinkedDisplayStates();
```

object renderMaterials = null

;

```vb
renderMaterials = swModelDocExt.GetRenderMaterials2((
```

int)swDisplayStateOpts_e.swAllDisplayState, null

);

// Examine the display states of the active configuration

// to ensure that the specified appearance was applied to all

// display states

// Continue running the macro after your examination

```vb
System.Diagnostics.
```

Debugger

.Break();

// Delete the appearance from the part

```vb
materialID1_ToDelete[0] = materialID1;
materialID2_ToDelete[0] = materialID2;
swModelDocExt.DeleteDisplayStateSpecificRenderMaterial((materialID1_ToDelete), (materialID2_ToDelete));
swModel.ForceRebuild3(
```

true

);

// Examine the display states of the active configuration

// to ensure that the specified appearance was deleted from all

// display states

// Continue running the macro after your examination

```vb
System.Diagnostics.
```

Debugger

.Break();

// Close the part without saving changes

```vb
modelName = swModel.GetTitle();
swApp.QuitDoc(modelName);
            }
```

public SldWorks

swApp;

```vb
        }
}
```
