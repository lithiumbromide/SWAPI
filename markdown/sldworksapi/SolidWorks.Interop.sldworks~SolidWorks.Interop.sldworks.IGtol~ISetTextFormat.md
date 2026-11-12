---
title: "ISetTextFormat Method (IGtol)"
project: "SOLIDWORKS API Help"
interface: "IGtol"
member: "ISetTextFormat"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~ISetTextFormat.html"
---

# ISetTextFormat Method (IGtol)

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
Dim instance As IGtol
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

See [Gtol::ISetTextFormat](ms-its:sldworksapivb6.chm::/sldworks~Gtol~ISetTextFormat.html).

## See Also

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.html)
[IGtol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.html)
