---
title: "SplitFaceOnParam Method (IModeler)"
project: "SOLIDWORKS API Help"
interface: "IModeler"
member: "SplitFaceOnParam"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~SplitFaceOnParam.html"
---

# SplitFaceOnParam Method (IModeler)

Splits and retrieves the faces on the U or V parameter

## Syntax

### Visual Basic (Declaration)

```vb
Function SplitFaceOnParam( _
   ByVal Facedisp As System.Object, _
   ByVal UVFlag As System.Integer, _
   ByVal Parameter As System.Double, _
   ByRef Status As System.Boolean _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModeler
Dim Facedisp As System.Object
Dim UVFlag As System.Integer
Dim Parameter As System.Double
Dim Status As System.Boolean
Dim value As System.Object

value = instance.SplitFaceOnParam(Facedisp, UVFlag, Parameter, Status)
```

### C#

```csharp
System.object SplitFaceOnParam(
   System.object Facedisp,
   System.int UVFlag,
   System.double Parameter,
   out System.bool Status
)
```

### C++/CLI

```cpp
System.Object^ SplitFaceOnParam(
   System.Object^ Facedisp,
   System.int UVFlag,
   System.double Parameter,
   [Out] System.bool Status
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Facedisp`: [Face](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) to split
- `UVFlag`: Parametric axis; either swSplitFaceOnParamU or swSplitFaceOnParamV
- `Parameter`: Position along the parametric axis at which the split is performed
- `Status`: True if the operation was successful, false if

### Return Value

Array of new [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html)

## VBA Syntax

See [Modeler::SplitFaceOnParam](ms-its:sldworksapivb6.chm::/sldworks~Modeler~SplitFaceOnParam.html).

## See Also

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.html)
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.html)
[IModeler::ISplitFaceOnParam2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ISplitFaceOnParam2.html)
[IModeler::ISplitFaceOnParamCount2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ISplitFaceOnParamCount2.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
