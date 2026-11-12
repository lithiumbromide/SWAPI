---
title: "IClearanceVerificationMgr Interface"
project: "SOLIDWORKS API Help"
interface: "IClearanceVerificationMgr"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceVerificationMgr.html"
---

# IClearanceVerificationMgr Interface

Allows you to check the clearance between selected components and/or faces in assemblies.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IClearanceVerificationMgr
```

### Visual Basic (Usage)

```vb
Dim instance As IClearanceVerificationMgr
```

### C#

```csharp
public interface IClearanceVerificationMgr
```

### C++/CLI

```cpp
public interface class IClearanceVerificationMgr
```

## VBA Syntax

See [ClearanceVerificationMgr](ms-its:sldworksapivb6.chm::/sldworks~ClearanceVerificationMgr.html).

## Examples

'VBA

'===================================================

'Preconditions:

'1. Open `Public_documents`**\SOLIDWORKS\SOLIDWORKS 2024\samples\tutorial\advdrawings\98food processor.sldasm**.

'2. In the FeatureManager design tree, multi-select gear-caddy and shaft gear components.

'3. Open an Immediate window.

'Postconditions: Inspect the Immediate window.

'================================================

Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim selMgr As SldWorks.SelectionMgr
Dim asmDoc As SldWorks.AssemblyDoc
Dim CVMgr As SldWorks.ClearanceVerificationMgr
Option Explicit

Sub main()

Set swApp = Application.SldWorks
Set swModel = swApp.**ActiveDoc**
Set asmDoc = swModel
Set CVMgr = asmDoc.**ClearanceVerificationManager**
Set selMgr = swModel.**SelectionManager**

Dim comp() As SldWorks.Component2
Dim faces() As SldWorks.Face2

ReDim comp(0)
ReDim faces(0)

Dim i As Long
For i = 0 To selMgr.**GetSelectedObjectCount**() - 1
If selMgr.**GetSelectedObjectType3**(i + 1, 0) = swSelectType_e.swSelCOMPONENTS Then
If (Not comp(UBound(comp)) Is Nothing) Then
ReDim Preserve comp(UBound(comp) + 1)
End If
Set comp(UBound(comp)) = selMgr.**GetSelectedObject6**(i + 1, -1)
Else
If selMgr.**GetSelectedObjectType3**(i + 1, 0) = swSelectType_e.swSelFACES Then
If (Not faces(UBound(faces)) Is Nothing) Then
ReDim Preserve faces(UBound(faces) + 1)
End If
Set faces(UBound(faces)) = selMgr.**GetSelectedObject6**(i + 1, -1)
Else
End
End If
End If
Next

Dim facesVar As Variant
Dim compsVar As Variant
If (Not comp(0) Is Nothing) Then
compsVar = comp
End If

If (Not faces(0) Is Nothing) Then
facesVar = faces
End If

Dim err As Long
Debug.Print "Successfully set components or faces to check: " & CVMgr.**SetComponentsOrFacesToCheck**(compsVar, facesVar, err)

Dim var As Variant
var = CVMgr.**GetComponentsOrFacesToCheck**()
Debug.Print "Number of entities to check: " & (UBound(var) + 1)

Debug.Print "Successfully set minimum acceptable clearance of 0.05 m: " & CVMgr.**SetMinimumAcceptableClearance**(0.05)
CVMgr.**CheckClearanceBetween** = swCheckClearanceBetweenSelectedItems
CVMgr.**TreatSubAssembliesAsComponents** = False
CVMgr.**IgnoreClearanceEqualToSpecifiedValue** = True

Dim ClearanceVar As Variant
ClearanceVar = CVMgr.**CalculateClearances**()

Dim iter As Integer
Dim clearance As ClearanceResult

For iter = 0 To UBound(ClearanceVar)
Set clearance = ClearanceVar(iter)

Dim clrObjVar As Variant
clrObjVar = clearance.**ComponentsOrFaces**
Debug.Print "Number of clearance result entities: " & (UBound(clrObjVar) + 1)
Dim clrObjs(2) As Object
Set clrObjs(0) = clrObjVar(0)
Set clrObjs(1) = clrObjVar(1)

Debug.Print "Clearance type as defined by swClearanceType_e: " & clearance.**ClearanceType**
Debug.Print "Clearance value (m): " & clearance.**ClearanceValue**
Next

End Sub

## Remarks

For more information see **SOLIDWORKS online Help > Assemblies > Detecting Problems > Clearance Verification**.

## Accessors

[IAssemblyDoc::ClearanceVerificationManager](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ClearanceVerificationManager.html)

## Access Diagram

[ClearanceVerificationMgr](SWObjectModel.pdf#ClearanceVerificationMgr)

## See Also

[IClearanceVerificationMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceVerificationMgr_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IClearanceResult Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceResult.html)
