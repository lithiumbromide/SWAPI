---
title: "GetOriginalPatternedBody Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "GetOriginalPatternedBody"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetOriginalPatternedBody.html"
---

# GetOriginalPatternedBody Method (IBody2)

Gets the original body from this patterned body. Also gets the transformation of this body with respect to the original body.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetOriginalPatternedBody( _
   ByRef Xform As MathTransform _
) As Body2
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim Xform As MathTransform
Dim value As Body2

value = instance.GetOriginalPatternedBody(Xform)
```

### C#

```csharp
Body2 GetOriginalPatternedBody(
   out MathTransform Xform
)
```

### C++/CLI

```cpp
Body2^ GetOriginalPatternedBody(
   [Out] MathTransform^ Xform
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Xform`: [IMathTransform](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathTransform.html)

### Return Value

[IBody2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html)

## VBA Syntax

See [Body2::GetOriginalPatternedBody](ms-its:sldworksapivb6.chm::/sldworks~Body2~GetOriginalPatternedBody.html).

## Examples

[Get Original Body from Pattern Body (VBA)](Get_Original_Body_from_Pattern_Body_Example_VB.htm)
[Get Original Body from Pattern Body (VB.NET)](Get_Original_Body_from_Pattern_Body_Example_VBNET.htm)
[Get Original Body from Pattern Body (C#)](Get_Original_Body_from_Pattern_Body_Example_CSharp.htm)

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)

## Availability

SOLIDWORKS 2011 SP01, Revision Number 19.1
