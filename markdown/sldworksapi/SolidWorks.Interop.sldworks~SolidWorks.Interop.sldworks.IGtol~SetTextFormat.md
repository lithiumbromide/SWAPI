---
title: "SetTextFormat Method (IGtol)"
project: "SOLIDWORKS API Help"
interface: "IGtol"
member: "SetTextFormat"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~SetTextFormat.html"
---

# SetTextFormat Method (IGtol)

Obsolete. Superseded by [IAnnotation::SetTextFormat](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation~SetTextFormat.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SetTextFormat( _
   ByVal TextFormatType As System.Integer, _
   ByVal TextFormat As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IGtol
Dim TextFormatType As System.Integer
Dim TextFormat As System.Object
Dim value As System.Boolean

value = instance.SetTextFormat(TextFormatType, TextFormat)
```

### C#

```csharp
System.bool SetTextFormat(
   System.int TextFormatType,
   System.object TextFormat
)
```

### C++/CLI

```cpp
System.bool SetTextFormat(
   System.int TextFormatType,
   System.Object^ TextFormat
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `TextFormatType`:
- `TextFormat`:

## VBA Syntax

See [Gtol::SetTextFormat](ms-its:sldworksapivb6.chm::/sldworks~Gtol~SetTextFormat.html).

## See Also

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.html)
[IGtol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.html)
