---
title: "ISectionBySheet Method (IBody)"
project: "SOLIDWORKS API Help"
interface: "IBody"
member: "ISectionBySheet"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody~ISectionBySheet.html"
---

# ISectionBySheet Method (IBody)

Obsolete. Superseded by [IBody2::ISectionBySheet](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~ISectionBySheet.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function ISectionBySheet( _
   ByVal Sheet As Body, _
   ByVal NumMaxSections As System.Integer, _
   ByRef SectionedBodies As Body _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IBody
Dim Sheet As Body
Dim NumMaxSections As System.Integer
Dim SectionedBodies As Body
Dim value As System.Integer

value = instance.ISectionBySheet(Sheet, NumMaxSections, SectionedBodies)
```

### C#

```csharp
System.int ISectionBySheet(
   Body Sheet,
   System.int NumMaxSections,
   ref Body SectionedBodies
)
```

### C++/CLI

```cpp
System.int ISectionBySheet(
   Body^ Sheet,
   System.int NumMaxSections,
   Body^% SectionedBodies
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Sheet`:
- `NumMaxSections`:
- `SectionedBodies`:

## VBA Syntax

See [Body::ISectionBySheet](ms-its:sldworksapivb6.chm::/sldworks~Body~ISectionBySheet.html).

## See Also

[IBody Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody.html)
[IBody Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody_members.html)
