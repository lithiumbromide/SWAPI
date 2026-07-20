---
title: "ICoordinateSystemElement Interface"
project: "SOLIDWORKS API Help"
interface: "ICoordinateSystemElement"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemElement.html"
---

# ICoordinateSystemElement Interface

Allows access to a coordinate system element.

**NOTE:**Click the**Members**link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ICoordinateSystemElement
```

### Visual Basic (Usage)

```vb
Dim instance As ICoordinateSystemElement
```

### C#

```csharp
public interface ICoordinateSystemElement
```

### C++/CLI

```cpp
public interface class ICoordinateSystemElement
```

## VBA Syntax

See

[CoordinateSystemElement](ms-its:sldworksapivb6.chm::/sldworks~CoordinateSystemElement.html)

.

## Examples

‘VBA

'---------------------------------------------------------------------

' Preconditions:

' 1. Open a part with a coordinate system.

' 2. Select any coordinate system element.

' 3. Open the Immediate window.

'

' Postconditions: Examine the Immediate window for the type of coordinate system element selected.

'---------------------------------------------------------------------

Option Explicit

Dim swApp As SldWorks.SldWorks

Dim swModel As SldWorks.ModelDoc2

Dim swSelMgr As SldWorks.SelectionMgr

Dim swFeat As SldWorks.Feature

Dim swComponent As SldWorks.Component2

Dim swCoordSysFeat As SldWorks.CoordinateSystemFeatureData

Dim iSelType As Long

Dim isCoordSysElmSelected As Boolean

Dim swCordSysElement As SldWorks.CoordinateSystemElement

Dim boolstatus As Boolean

Sub main()

Set swApp = Application.SldWorks

Set swModel = swApp.ActiveDoc

'boolstatus = swModel.Extension.SelectByID2("Coordinate System1\X Axis", "COORDSYS", 0, 0, 0, False, 0, Nothing, 0)

'Select any coordinate system element

'Stop

Set swSelMgr = swModel.SelectionManager

Set swComponent = swSelMgr.GetSelectedObjectsComponent4(1, -1)

iSelType = swSelMgr.GetSelectedObjectType3(1, -1)

If iSelType = swSelCOORDSYS Then

isCoordSysElmSelected = swSelMgr. IsCoordSysElementSelected (1, -1)

If isCoordSysElmSelected = True Then

Set swCordSysElement = swSelMgr. GetSelectedCoordSysElement (1, -1)

Dim ElementType As Long

ElementType = swCordSysElement. GetElementType

Debug.Print "ElementType: " & ElementType

Set swFeat = swCordSysElement. GetCoordinateSystem

Set swCoordSysFeat = swFeat.GetDefinition

swCoordSysFeat.AccessSelections swModel, swComponent

'Stop

swCoordSysFeat.ReleaseSelectionAccess

End If

End If

End Sub

## Remarks

The normal channel of feature editing (IFeature::CreateDefinition, IFeature::ModifyDefinition) will not work for features created with coordinate system elements. In order to edit a feature created with a coordinate system element, you must:

1. Select the feature created with a coordinate system element.
2. Call the IModelDocExtension::RunCommand swCommands_e.swCommands_EditFeature to open a PropertyManager dialog for the selected object.
3. Call ISelectionMgr::GetSelectedObjectType3 to obtain the selection.
4. Test whether the selection is a coordinate system element.
5. If the selection is a coordinate system element, obtain the CoordinateSystemElement object.

'VBA

'---------------------------------------------------------------------
' Preconditions:
' 1. Open a part that contains an Axis1 created using a coordinate system element.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Examine the Immediate window to see the coordinate system element type as defined by swCoordSysElementType_e.
' 2. Examine the user interface. The specified coordinate system element should be selected.
'
'---------------------------------------------------------------------
Option Explicit
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swSelMgr As SldWorks.SelectionMgr
Dim iSelType As Long
Dim isCoordSysElmSelected As Boolean
Dim swCordSysElement As SldWorks.CoordinateSystemElement
Dim boolstatus As Boolean

Sub main()

Set swApp = Application.SldWorks

Set swModel = swApp.ActiveDoc
boolstatus = swModel.Extension.SelectByID2("Axis1", "AXIS", 0, 0, 0, False, 0, Nothing, 0)
swModel.Extension.RunCommand swCommands_e.swCommands_EditFeature, ""

Set swSelMgr = swModel.SelectionManager
iSelType = swSelMgr.GetSelectedObjectType3(1, -1)

If iSelType = swSelCOORDSYS Then

isCoordSysElmSelected = swSelMgr.IsCoordSysElementSelected(1, -1)

If isCoordSysElmSelected Then

Set swCordSysElement = swSelMgr.GetSelectedCoordSysElement(1, -1)
Debug.Print "Element type: " & swCordSysElement.GetElementType

End If

End If
swModel.Extension.RunCommand swCommands_e.swCommands_Dve_Rmb_Cancel, ""
Set swCordSysElement = Nothing

End Sub

## Accessors

[ISelectionMgr::GetSelectedCoordSysElement](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedCoordSysElement.html)

## Access Diagram

[CoordinateSystemElement](SWObjectModel.pdf#CoordinateSystemElement)

## See Also

[ICoordinateSystemElement Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemElement_members.html)

[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
