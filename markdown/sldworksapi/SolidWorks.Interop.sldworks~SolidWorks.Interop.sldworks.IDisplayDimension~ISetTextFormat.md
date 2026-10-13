---
title: "ISetTextFormat Method (IDisplayDimension)"
project: "SOLIDWORKS API Help"
interface: "IDisplayDimension"
member: "ISetTextFormat"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~ISetTextFormat.html"
---

# ISetTextFormat Method (IDisplayDimension)

Obsolete. Superseded by [IAnnotation::ISetTextFormat](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation~ISetTextFormat.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function ISetTextFormat( _
   ByVal TextFormatType As System.Integer, _
   ByVal TextFormat As TextFormat _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayDimension
Dim TextFormatType As System.Integer
Dim TextFormat As TextFormat
Dim value As System.Boolean

value = instance.ISetTextFormat(TextFormatType, TextFormat)
```

### C#

```csharp
System.bool ISetTextFormat(
   System.int TextFormatType,
   TextFormat TextFormat
)
```

### C++/CLI

```cpp
System.bool ISetTextFormat(
   System.int TextFormatType,
   TextFormat^ TextFormat
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `TextFormatType`:
- `TextFormat`:

## VBA Syntax

See [DisplayDimension::ISetTextFormat](ms-its:sldworksapivb6.chm::/sldworks~DisplayDimension~ISetTextFormat.html).

## See Also

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.html)
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.html)
