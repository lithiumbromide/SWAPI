---
title: "GetAnnotation Method (IWeldSymbol)"
project: "SOLIDWORKS API Help"
interface: "IWeldSymbol"
member: "GetAnnotation"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~GetAnnotation.html"
---

# GetAnnotation Method (IWeldSymbol)

Gets the annotation for this weld symbol.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetAnnotation() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IWeldSymbol
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

[Annotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation.html)

## VBA Syntax

See [WeldSymbol::GetAnnotation](ms-its:sldworksapivb6.chm::/sldworks~WeldSymbol~GetAnnotation.html).

## Examples

[Get Annotation Object (VBA)](Get_Annotation_Object_Example_VB.htm)
[Get Annotation Object (VB.NET)](Get_Annotation_Object_Example_VBNET.htm)
[Get Annotation Object (C#)](Get_Annotation_Object_Example_CSharp.htm)

## Remarks

This method obtains the owning [IAnnotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation.html) object, which is a higher-level object that contains methods that are general to all types of annotations.

## See Also

[IWeldSymbol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol.html)
[IWeldSymbol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol_members.html)
[IWeldSymbol::IGetAnnotation Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~IGetAnnotation.html)

## Availability

SOLIDWORKS 99, datecode 1999207
