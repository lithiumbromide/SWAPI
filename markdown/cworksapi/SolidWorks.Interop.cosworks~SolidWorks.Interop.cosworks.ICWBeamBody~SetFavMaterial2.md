---
title: "SetFavMaterial2 Method (ICWBeamBody)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBeamBody"
member: "SetFavMaterial2"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamBody~SetFavMaterial2.html"
---

# SetFavMaterial2 Method (ICWBeamBody)

Applies the specified material from the material favorites list.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetFavMaterial2( _
   ByVal NFav As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBeamBody
Dim NFav As System.Integer
Dim value As System.Boolean

value = instance.SetFavMaterial2(NFav)
```

### C#

```csharp
System.bool SetFavMaterial2(
   System.int NFav
)
```

### C++/CLI

```cpp
System.bool SetFavMaterial2(
   System.int NFav
)
```

### Parameters

- `NFav`: 1 <= index of material in favorites list <= 100 (see **Remarks**)

### Return Value

-1 or true if material applied successfully, 0 or false if not

## Remarks

This method returns a boolean value that can be cast to an integer.

The list of material favorites appears when you right-click a component in the Simulation study tree and click **Apply Favorite Material**.

## See Also

[ICWBeamBody Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamBody.html)
[ICWBeamBody Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamBody_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
