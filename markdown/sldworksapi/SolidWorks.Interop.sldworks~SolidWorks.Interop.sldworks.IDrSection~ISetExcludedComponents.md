---
title: "ISetExcludedComponents Method (IDrSection)"
project: "SOLIDWORKS API Help"
interface: "IDrSection"
member: "ISetExcludedComponents"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~ISetExcludedComponents.html"
---

# ISetExcludedComponents Method (IDrSection)

Excludes the specified components from this section view.

## Syntax

### Visual Basic (Declaration)

```vb
Function ISetExcludedComponents( _
   ByVal Number As System.Integer, _
   ByRef LpComps As Component _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDrSection
Dim Number As System.Integer
Dim LpComps As Component
Dim value As System.Boolean

value = instance.ISetExcludedComponents(Number, LpComps)
```

### C#

```csharp
System.bool ISetExcludedComponents(
   System.int Number,
   ref Component LpComps
)
```

### C++/CLI

```cpp
System.bool ISetExcludedComponents(
   System.int Number,
   Component^% LpComps
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Number`: Number of components
- `LpComps`: - in-process, unmanaged C++: Pointer to array of [IComponent2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2.html) objects of size Number

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

### Return Value

True if the specified components are excluded, false if not

## Remarks

Call [IModelDoc2::EditRebuild3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~EditRebuild3.html) after calling this method.

## See Also

[IDrSection Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection.html)
[IDrSection Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection_members.html)
[IDrSection::EnumExcludedComponents2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~EnumExcludedComponents2.html)
[IDrSection::GetExcludedComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~GetExcludedComponents.html)
[IDrSection::SetExcludedComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~SetExcludedComponents.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
