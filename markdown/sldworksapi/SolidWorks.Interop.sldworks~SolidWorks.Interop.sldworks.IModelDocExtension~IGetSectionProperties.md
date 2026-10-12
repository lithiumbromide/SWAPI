---
title: "IGetSectionProperties Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "IGetSectionProperties"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetSectionProperties.html"
---

# IGetSectionProperties Method (IModelDocExtension)

Obsolete. Superseded by [IModelDocExtension::IGetSectionProperties2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~IGetSectionProperties2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetSectionProperties( _
   ByVal Count As System.Integer, _
   ByRef Sections As System.Object _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim Count As System.Integer
Dim Sections As System.Object
Dim value As System.Double

value = instance.IGetSectionProperties(Count, Sections)
```

### C#

```csharp
System.double IGetSectionProperties(
   System.int Count,
   ref System.object Sections
)
```

### C++/CLI

```cpp
System.double IGetSectionProperties(
   System.int Count,
   System.Object^% Sections
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`:
- `Sections`:

## VBA Syntax

See [ModelDocExtension::IGetSectionProperties](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~IGetSectionProperties.html).

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
