---
title: "EnumExcludedComponents2 Method (IDrSection)"
project: "SOLIDWORKS API Help"
interface: "IDrSection"
member: "EnumExcludedComponents2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~EnumExcludedComponents2.html"
---

# EnumExcludedComponents2 Method (IDrSection)

Gets all of the assembly components that are excluded from this section view.

## Syntax

### Visual Basic (Declaration)

```vb
Function EnumExcludedComponents2() As EnumComponents2
```

### Visual Basic (Usage)

```vb
Dim instance As IDrSection
Dim value As EnumComponents2

value = instance.EnumExcludedComponents2()
```

### C#

```csharp
EnumComponents2 EnumExcludedComponents2()
```

### C++/CLI

```cpp
EnumComponents2^ EnumExcludedComponents2();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Pointer to the [IEnumComponents2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEnumComponents2.html) object

## VBA Syntax

See [DrSection::EnumExcludedComponents2](ms-its:sldworksapivb6.chm::/sldworks~DrSection~EnumExcludedComponents2.html).

## Remarks

The ability to exclude components applies only to assembly section views. This method returns NULL for section views of parts.

## See Also

[IDrSection Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection.html)
[IDrSection Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection_members.html)
[IDrSection::GetExcludedComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~GetExcludedComponents.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
