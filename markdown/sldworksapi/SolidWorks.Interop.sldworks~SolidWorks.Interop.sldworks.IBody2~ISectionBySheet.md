---
title: "ISectionBySheet Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "ISectionBySheet"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ISectionBySheet.html"
---

# ISectionBySheet Method (IBody2)

Sections a body using a sheet (surface) body.

## Syntax

### Visual Basic (Declaration)

```vb
Function ISectionBySheet( _
   ByVal Sheet As Body2, _
   ByVal NumMaxSections As System.Integer, _
   ByRef SectionedBodies As Body2 _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim Sheet As Body2
Dim NumMaxSections As System.Integer
Dim SectionedBodies As Body2
Dim value As System.Integer

value = instance.ISectionBySheet(Sheet, NumMaxSections, SectionedBodies)
```

### C#

```csharp
System.int ISectionBySheet(
   Body2 Sheet,
   System.int NumMaxSections,
   ref Body2 SectionedBodies
)
```

### C++/CLI

```cpp
System.int ISectionBySheet(
   Body2^ Sheet,
   System.int NumMaxSections,
   Body2^% SectionedBodies
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Sheet`: Pointer to the sheet body used to perform the section
- `NumMaxSections`: Maximum number of sections to create
- `SectionedBodies`: Pointer to an array of [bodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html) created during the section operation

### Return Value

Number of bodies created during the operation

## VBA Syntax

See [Body2::ISectionBySheet](ms-its:sldworksapivb6.chm::/sldworks~Body2~ISectionBySheet.html).

## Remarks

Before using this method, [make a copy of the body](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~Copy.html) because the sheet body becomes invalid after using this method. COM applications should release all bodies after calling this method.

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
