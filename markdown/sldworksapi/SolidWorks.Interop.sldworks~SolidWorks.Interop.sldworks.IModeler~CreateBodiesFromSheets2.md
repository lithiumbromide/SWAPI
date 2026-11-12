---
title: "CreateBodiesFromSheets2 Method (IModeler)"
project: "SOLIDWORKS API Help"
interface: "IModeler"
member: "CreateBodiesFromSheets2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBodiesFromSheets2.html"
---

# CreateBodiesFromSheets2 Method (IModeler)

Sews sheets to make sheet (surface) or solid bodies.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateBodiesFromSheets2( _
   ByVal Sheets As System.Object, _
   ByVal Options As System.Integer, _
   ByVal KnittingTolerance As System.Double, _
   ByRef Error As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModeler
Dim Sheets As System.Object
Dim Options As System.Integer
Dim KnittingTolerance As System.Double
Dim Error As System.Integer
Dim value As System.Object

value = instance.CreateBodiesFromSheets2(Sheets, Options, KnittingTolerance, Error)
```

### C#

```csharp
System.object CreateBodiesFromSheets2(
   System.object Sheets,
   System.int Options,
   System.double KnittingTolerance,
   out System.int Error
)
```

### C++/CLI

```cpp
System.Object^ CreateBodiesFromSheets2(
   System.Object^ Sheets,
   System.int Options,
   System.double KnittingTolerance,
   [Out] System.int Error
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Sheets`: Array containing the [shee](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html)ts
- `Options`: Type of body to create as defined by [swSheetSewingOption_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSheetSewingOption_e.html)
- `KnittingTolerance`: Knitting tolerance
- `Error`: Error as defined by [swSheetSewingError_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSheetSewingError_e.html)

### Return Value

Array of the sheet or solid [bodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html)

## VBA Syntax

See [Modeler::CreateBodiesFromSheets2](ms-its:sldworksapivb6.chm::/sldworks~Modeler~CreateBodiesFromSheets2.html).

## Remarks

It is safest to assume that the maximum number of bodies that can be returned by this method is the number of sheet input bodies.

## See Also

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.html)
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.html)
[IModeler::ICreateBodiesFromSheets2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBodiesFromSheets2.html)
[IModeler::ICreateBodyFromBox2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBodyFromBox2.html)
[IModeler::ICreateBodyFromCone2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBodyFromCone2.html)
[IModeler::ICreateBodyFromCyl2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBodyFromCyl2.html)
[IModeler::ICreateBodyFromFaces3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBodyFromFaces3.html)
[IModeler::ICreateBrepBody3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBrepBody3.html)
[IModeler::ICreateWireBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateWireBody.html)
[IModeler::CreateBodyFromBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBodyFromBox.html)
[IModeler::CreateBodyFromCone Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBodyFromCone.html)
[IModeler::CreateBodyFromCyl Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBodyFromCyl.html)
[IModeler::CreateBodyFromFaces2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBodyFromFaces2.html)
[IModeler::CreateBrepBody3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBrepBody3.html)
[IModeler::CreateExtrudedBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateExtrudedBody.html)
[IModeler::CreateSweptBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateSweptBody.html)
[IModeler::CreateWireBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateWireBody.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
