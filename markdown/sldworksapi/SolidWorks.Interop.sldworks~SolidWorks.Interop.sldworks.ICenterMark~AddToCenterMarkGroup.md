---
title: "AddToCenterMarkGroup Method (ICenterMark)"
project: "SOLIDWORKS API Help"
interface: "ICenterMark"
member: "AddToCenterMarkGroup"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark~AddToCenterMarkGroup.html"
---

# AddToCenterMarkGroup Method (ICenterMark)

Adds a center mark for the selected entity in an existing center mark set.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddToCenterMarkGroup() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICenterMark
Dim value As System.Boolean

value = instance.AddToCenterMarkGroup()
```

### C#

```csharp
System.bool AddToCenterMarkGroup()
```

### C++/CLI

```cpp
System.bool AddToCenterMarkGroup();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if a center mark is added for the selected entity in an existing center mark set, false if not (see **Remarks**)

## VBA Syntax

See [CenterMark::AddToCenterMarkGroup](ms-its:sldworksapivb6.chm::/sldworks~CenterMark~AddToCenterMarkGroup.html).

## Remarks

You must pre-select an entity in an existing center mark set (i.e., a linear or circular pattern) for which to add a center mark. If the existing center mark set is a linear pattern, then the selected entity must be in that linear pattern, else this method fails. The same rule applies when adding an entity to an existing center mark set that is a circular pattern.

To determine if a center mark is in a center mark set, use [ICenterMark::IsGrouped](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark~IsGrouped.html).

## See Also

[ICenterMark Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark.html)
[ICenterMark Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark_members.html)
[ICenterMark::GroupCount Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark~GroupCount.html)
[ICenterMark::HasDetachCenterMark Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark~HasDetachCenterMark.html)
[ICenterMark::IsDetached Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark~IsDetached.html)
[ICenterMark::ReattachToCenterMarkGroup Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark~ReattachToCenterMarkGroup.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
