---
title: "Make3DExperienceCompatible Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "Make3DExperienceCompatible"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~Make3DExperienceCompatible.html"
---

# Make3DExperienceCompatible Method (IModelDocExtension)

Makes the current model compatible with [SOLIDWORKS Design connected to the 3DEXPERIENCE platform](ms-its:sldworksapiprogguide.chm:://Overview/SOLIDWORKS_Connected.htm).

## Syntax

### Visual Basic (Declaration)

```vb
Sub Make3DExperienceCompatible( _
   ByVal IncludeComponents As System.Boolean, _
   ByRef Result As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim IncludeComponents As System.Boolean
Dim Result As System.Boolean

instance.Make3DExperienceCompatible(IncludeComponents, Result)
```

### C#

```csharp
void Make3DExperienceCompatible(
   System.bool IncludeComponents,
   out System.bool Result
)
```

### C++/CLI

```cpp
void Make3DExperienceCompatible(
   System.bool IncludeComponents,
   [Out] System.bool Result
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `IncludeComponents`: True to make components compatible with 3DExperience, false to not
- `Result`: True if model successfully made compatible with 3DExperience, false if not

## VBA Syntax

See [ModelDocExtension::Make3DExperienceCompatible](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~Make3DExperienceCompatible.html).

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)

## Availability

SOLIDWORKS 2022 SP01, Revision Number 30.1
