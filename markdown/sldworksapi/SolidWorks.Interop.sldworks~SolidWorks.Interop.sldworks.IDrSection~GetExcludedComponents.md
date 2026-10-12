---
title: "GetExcludedComponents Method (IDrSection)"
project: "SOLIDWORKS API Help"
interface: "IDrSection"
member: "GetExcludedComponents"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~GetExcludedComponents.html"
---

# GetExcludedComponents Method (IDrSection)

Gets all of the assembly components that are excluded from this section view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetExcludedComponents() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IDrSection
Dim value As System.Object

value = instance.GetExcludedComponents()
```

### C#

```csharp
System.object GetExcludedComponents()
```

### C++/CLI

```cpp
System.Object^ GetExcludedComponents();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of excluded [components](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2.html)

## VBA Syntax

See [DrSection::GetExcludedComponents](ms-its:sldworksapivb6.chm::/sldworks~DrSection~GetExcludedComponents.html).

## See Also

[IDrSection Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection.html)
[IDrSection Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection_members.html)
[IDrSection::EnumExcludedComponents2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~EnumExcludedComponents2.html)
[IDrSection::ISetExcludedComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~ISetExcludedComponents.html)
[IDrSection::SetExcludedComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~SetExcludedComponents.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
