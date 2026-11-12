---
title: "SetExcludedComponents Method (IDrSection)"
project: "SOLIDWORKS API Help"
interface: "IDrSection"
member: "SetExcludedComponents"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~SetExcludedComponents.html"
---

# SetExcludedComponents Method (IDrSection)

Excludes the specified components from this section view.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetExcludedComponents( _
   ByVal VComponents As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDrSection
Dim VComponents As System.Object
Dim value As System.Boolean

value = instance.SetExcludedComponents(VComponents)
```

### C#

```csharp
System.bool SetExcludedComponents(
   System.object VComponents
)
```

### C++/CLI

```cpp
System.bool SetExcludedComponents(
   System.Object^ VComponents
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `VComponents`: Array of [components](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2.html)

### Return Value

True if the specified components are excluded, false if not

## VBA Syntax

See [DrSection::SetExcludedComponents](ms-its:sldworksapivb6.chm::/sldworks~DrSection~SetExcludedComponents.html).

## See Also

[IDrSection Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection.html)
[IDrSection Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection_members.html)
[IDrSection::EnumExcludedComponents2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~EnumExcludedComponents2.html)
[IDrSection::GetExcludedComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~GetExcludedComponents.html)
[IDrSection::ISetExcludedComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~ISetExcludedComponents.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
