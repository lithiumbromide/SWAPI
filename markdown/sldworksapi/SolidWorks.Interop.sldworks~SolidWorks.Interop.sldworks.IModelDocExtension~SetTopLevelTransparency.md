---
title: "SetTopLevelTransparency Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "SetTopLevelTransparency"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetTopLevelTransparency.html"
---

# SetTopLevelTransparency Method (IModelDocExtension)

Sets the transparency of this part or top-level assembly.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetTopLevelTransparency( _
   ByVal InValue As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim InValue As System.Boolean
Dim value As System.Boolean

value = instance.SetTopLevelTransparency(InValue)
```

### C#

```csharp
System.bool SetTopLevelTransparency(
   System.bool InValue
)
```

### C++/CLI

```cpp
System.bool SetTopLevelTransparency(
   System.bool InValue
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `InValue`: True to make this part or top-level assembly transparent, false to not

### Return Value

True if transparency of this part or top-level assembly successfully set, false if not

## VBA Syntax

See [ModelDocExtension::SetTopLevelTransparency](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~SetTopLevelTransparency.html).

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
