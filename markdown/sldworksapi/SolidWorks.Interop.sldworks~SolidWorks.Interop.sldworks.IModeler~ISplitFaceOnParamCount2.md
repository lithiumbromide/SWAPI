---
title: "ISplitFaceOnParamCount2 Method (IModeler)"
project: "SOLIDWORKS API Help"
interface: "IModeler"
member: "ISplitFaceOnParamCount2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ISplitFaceOnParamCount2.html"
---

# ISplitFaceOnParamCount2 Method (IModeler)

Sets up and counts the number of new faces split on the U or V parameter.

## Syntax

### Visual Basic (Declaration)

```vb
Function ISplitFaceOnParamCount2( _
   ByVal Facedisp As Face2, _
   ByVal UVFlag As System.Integer, _
   ByVal Parameter As System.Double, _
   ByRef Status As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModeler
Dim Facedisp As Face2
Dim UVFlag As System.Integer
Dim Parameter As System.Double
Dim Status As System.Boolean
Dim value As System.Integer

value = instance.ISplitFaceOnParamCount2(Facedisp, UVFlag, Parameter, Status)
```

### C#

```csharp
System.int ISplitFaceOnParamCount2(
   Face2 Facedisp,
   System.int UVFlag,
   System.double Parameter,
   out System.bool Status
)
```

### C++/CLI

```cpp
System.int ISplitFaceOnParamCount2(
   Face2^ Facedisp,
   System.int UVFlag,
   System.double Parameter,
   [Out] System.bool Status
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Facedisp`: [Face](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) to split
- `UVFlag`: Parametric axis; either swSplitFaceOnParamU or swSplitFaceOnParamV
- `Parameter`: Position along the parametric axis at which the split will be performed
- `Status`: True if the operation was successful, false if not

### Return Value

Number of new faces

## VBA Syntax

See [Modeler::ISplitFaceOnParamCount2](ms-its:sldworksapivb6.chm::/sldworks~Modeler~ISplitFaceOnParamCount2.html).

## Remarks

The split is defined by calling this method. Then, you can retrieve the list of new faces by using [IModeler::ISplitFaceOnParam2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~ISplitFaceOnParam2.html).

## See Also

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.html)
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.html)
[IModeler::SplitFaceOnParam Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~SplitFaceOnParam.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
