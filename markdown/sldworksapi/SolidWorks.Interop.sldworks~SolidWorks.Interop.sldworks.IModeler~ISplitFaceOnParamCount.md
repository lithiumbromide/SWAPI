---
title: "ISplitFaceOnParamCount Method (IModeler)"
project: "SOLIDWORKS API Help"
interface: "IModeler"
member: "ISplitFaceOnParamCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ISplitFaceOnParamCount.html"
---

# ISplitFaceOnParamCount Method (IModeler)

Obsolete. Superseded by [IModeler::ISplitFaceOnParamCount2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~ISplitFaceOnParamCount2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function ISplitFaceOnParamCount( _
   ByVal Facedisp As Face, _
   ByVal UVFlag As System.Integer, _
   ByVal Parameter As System.Double, _
   ByRef Status As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModeler
Dim Facedisp As Face
Dim UVFlag As System.Integer
Dim Parameter As System.Double
Dim Status As System.Boolean
Dim value As System.Integer

value = instance.ISplitFaceOnParamCount(Facedisp, UVFlag, Parameter, Status)
```

### C#

```csharp
System.int ISplitFaceOnParamCount(
   Face Facedisp,
   System.int UVFlag,
   System.double Parameter,
   out System.bool Status
)
```

### C++/CLI

```cpp
System.int ISplitFaceOnParamCount(
   Face^ Facedisp,
   System.int UVFlag,
   System.double Parameter,
   [Out] System.bool Status
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Facedisp`:
- `UVFlag`:
- `Parameter`:
- `Status`:

## VBA Syntax

See [Modeler::ISplitFaceOnParamCount](ms-its:sldworksapivb6.chm::/sldworks~Modeler~ISplitFaceOnParamCount.html).

## See Also

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.html)
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.html)
