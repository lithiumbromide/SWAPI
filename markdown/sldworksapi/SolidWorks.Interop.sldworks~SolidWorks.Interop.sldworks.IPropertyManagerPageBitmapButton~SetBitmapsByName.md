---
title: "SetBitmapsByName Method (IPropertyManagerPageBitmapButton)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageBitmapButton"
member: "SetBitmapsByName"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageBitmapButton~SetBitmapsByName.html"
---

# SetBitmapsByName Method (IPropertyManagerPageBitmapButton)

Obsolete. Superseded by [IPropertyManagerPageBitmapButton::SetBitmapsByName2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPageBitmapButton~SetBitmapsByName2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SetBitmapsByName( _
   ByVal BitmapUp As System.String, _
   ByVal BitmapDown As System.String, _
   ByVal BitmapDisabled As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPageBitmapButton
Dim BitmapUp As System.String
Dim BitmapDown As System.String
Dim BitmapDisabled As System.String
Dim value As System.Boolean

value = instance.SetBitmapsByName(BitmapUp, BitmapDown, BitmapDisabled)
```

### C#

```csharp
System.bool SetBitmapsByName(
   System.string BitmapUp,
   System.string BitmapDown,
   System.string BitmapDisabled
)
```

### C++/CLI

```cpp
System.bool SetBitmapsByName(
   System.String^ BitmapUp,
   System.String^ BitmapDown,
   System.String^ BitmapDisabled
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `BitmapUp`:
- `BitmapDown`:
- `BitmapDisabled`:

## VBA Syntax

See [PropertyManagerPageBitmapButton::SetBitmapsByName](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPageBitmapButton~SetBitmapsByName.html).

## See Also

[IPropertyManagerPageBitmapButton Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageBitmapButton.html)
[IPropertyManagerPageBitmapButton Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageBitmapButton_members.html)
