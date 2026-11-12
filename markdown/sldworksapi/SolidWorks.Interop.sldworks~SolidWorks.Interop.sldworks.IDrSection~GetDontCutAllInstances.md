---
title: "GetDontCutAllInstances Method (IDrSection)"
project: "SOLIDWORKS API Help"
interface: "IDrSection"
member: "GetDontCutAllInstances"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~GetDontCutAllInstances.html"
---

# GetDontCutAllInstances Method (IDrSection)

Gets whether all instances of the specified component are uncut in this section view or only in the specified component.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDontCutAllInstances( _
   ByVal LpComp As Component _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDrSection
Dim LpComp As Component
Dim value As System.Boolean

value = instance.GetDontCutAllInstances(LpComp)
```

### C#

```csharp
System.bool GetDontCutAllInstances(
   Component LpComp
)
```

### C++/CLI

```cpp
System.bool GetDontCutAllInstances(
   Component^ LpComp
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `LpComp`: Pointer to the [IComponent2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2.html) object

### Return Value

True if all instances of the selected component are left uncut, false if only the selected component is left uncut

## VBA Syntax

See [DrSection::GetDontCutAllInstances](ms-its:sldworksapivb6.chm::/sldworks~DrSection~GetDontCutAllInstances.html).

## See Also

[IDrSection Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection.html)
[IDrSection Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection_members.html)
[IDrSection::SetDontCutAllInstances Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~SetDontCutAllInstances.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
