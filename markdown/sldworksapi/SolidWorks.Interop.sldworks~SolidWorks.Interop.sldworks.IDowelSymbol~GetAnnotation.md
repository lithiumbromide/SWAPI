---
title: "GetAnnotation Method (IDowelSymbol)"
project: "SOLIDWORKS API Help"
interface: "IDowelSymbol"
member: "GetAnnotation"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDowelSymbol~GetAnnotation.html"
---

# GetAnnotation Method (IDowelSymbol)

Gets the IAnnotation object for this dowel symbol.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetAnnotation() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IDowelSymbol
Dim value As System.Object

value = instance.GetAnnotation()
```

### C#

```csharp
System.object GetAnnotation()
```

### C++/CLI

```cpp
System.Object^ GetAnnotation();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[Annotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.html)

## VBA Syntax

See [DowelSymbol::GetAnnotation](ms-its:sldworksapivb6.chm::/sldworks~DowelSymbol~GetAnnotation.html).

## Examples

[Get Annotation Object (VBA)](Get_Annotation_Object_Example_VB.htm)
[Get Annotation Object (VB.NET)](Get_Annotation_Object_Example_VBNET.htm)
[Get Annotation Object (C#)](Get_Annotation_Object_Example_CSharp.htm)
[Flip Dowel Pin Symbol (C#)](Flip_Dowel_Pin_Symbol_Example_CSharp.htm)
[Flip Dowel Pin Symbol (VB.NET)](Flip_Dowel_Pin_Symbol_Example_VBNET.htm)
[Flip Dowel Pin Symbol (VBA)](Flip_Dowel_Pin_Symbol_Example_VB.htm)

## See Also

[IDowelSymbol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDowelSymbol.html)
[IDowelSymbol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDowelSymbol_members.html)
[IDowelSymbol::IGetAnnotation Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDowelSymbol~IGetAnnotation.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
