---
title: "ICreateBodiesFromSheets2 Method (IModeler)"
project: "SOLIDWORKS API Help"
interface: "IModeler"
member: "ICreateBodiesFromSheets2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBodiesFromSheets2.html"
---

# ICreateBodiesFromSheets2 Method (IModeler)

Sews sheets to make a sheet (surface) or solid bodies.

## Syntax

### Visual Basic (Declaration)

```vb
Function ICreateBodiesFromSheets2( _
   ByVal NSheets As System.Integer, _
   ByRef Sheets As Body2, _
   ByVal Options As System.Integer, _
   ByVal KnittingTolerance As System.Double, _
   ByRef NResults As System.Integer, _
   ByRef Results As Body2 _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModeler
Dim NSheets As System.Integer
Dim Sheets As Body2
Dim Options As System.Integer
Dim KnittingTolerance As System.Double
Dim NResults As System.Integer
Dim Results As Body2
Dim value As System.Integer

value = instance.ICreateBodiesFromSheets2(NSheets, Sheets, Options, KnittingTolerance, NResults, Results)
```

### C#

```csharp
System.int ICreateBodiesFromSheets2(
   System.int NSheets,
   ref Body2 Sheets,
   System.int Options,
   System.double KnittingTolerance,
   out System.int NResults,
   out Body2 Results
)
```

### C++/CLI

```cpp
System.int ICreateBodiesFromSheets2(
   System.int NSheets,
   Body2^% Sheets,
   System.int Options,
   System.double KnittingTolerance,
   [Out] System.int NResults,
   [Out] Body2^ Results
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NSheets`: Number of sheets
- `Sheets`: Array containing the [sheets](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html)
- `Options`: Type of body to create as defined by [swSheetSewingOption_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSheetSewingOption_e.html)
- `KnittingTolerance`: Knitting tolerance
- `NResults`: Number of sheet or solid bodies created
- `Results`: Array of the sheet or solid [bodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html)

### Return Value

Error as defined by [swSheetSewingError_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSheetSewingError_e.html)

## VBA Syntax

See [Modeler::ICreateBodiesFromSheets2](ms-its:sldworksapivb6.chm::/sldworks~Modeler~ICreateBodiesFromSheets2.html).

## Remarks

It is safest to assume that the maximum number of bodies that can be returned by this method is the number of sheet input bodies. Your code should look like this:

```vb
aBodies = new IBody2*[lNumSheetBodies];
hres = swModeler->ICreateBodiesFromSheets2(lNumSheetBodies, aSheetBodies, swSewToSheets, 1e-6, &lNumBodies, aBodies, &lErrors);
```

## See Also

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.html)
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.html)
[IModeler::CreateBodiesFromSheets2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBodiesFromSheets2.html)
[IModeler::CreateBodyFromBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBodyFromBox.html)
[IModeler::CreateBodyFromCone Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBodyFromCone.html)
[IModeler::CreateBodyFromCyl Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBodyFromCyl.html)
[IModeler::CreateBodyFromFaces2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBodyFromFaces2.html)
[IModeler::CreateBrepBody3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBrepBody3.html)
[IModeler::CreateExtrudedBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateExtrudedBody.html)
[IModeler::CreateSweptBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateSweptBody.html)
[IModeler::CreateWireBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateWireBody.html)
[IModeler::ICreateBodyFromBox2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBodyFromBox2.html)
[IModeler::ICreateBodyFromCone2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBodyFromCone2.html)
[IModeler::ICreateBodyFromCyl2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBodyFromCyl2.html)
[IModeler::ICreateBodyFromFaces3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBodyFromFaces3.html)
[IModeler::ICreateBrepBody3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBrepBody3.html)
[IModeler::ICreateWireBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateWireBody.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
