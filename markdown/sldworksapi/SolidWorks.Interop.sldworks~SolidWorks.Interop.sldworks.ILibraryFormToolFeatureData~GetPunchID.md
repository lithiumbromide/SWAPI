---
title: "GetPunchID Method (ILibraryFormToolFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILibraryFormToolFeatureData"
member: "GetPunchID"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFormToolFeatureData~GetPunchID.html"
---

# GetPunchID Method (ILibraryFormToolFeatureData)

Gets the punch ID assigned to the Design Library forming tool.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPunchID() As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ILibraryFormToolFeatureData
Dim value As System.String

value = instance.GetPunchID()
```

### C#

```csharp
System.string GetPunchID()
```

### C++/CLI

```cpp
System.String^ GetPunchID();
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Return Value

Punch ID

## VBA Syntax

See

[LibraryFormToolFeatureData::GetPunchID](ms-its:sldworksapivb6.chm::/sldworks~LibraryFormToolFeatureData~GetPunchID.html)

.

## Examples

See the

[ILibraryFormToolFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFormToolFeatureData.html)

examples.

## Remarks

Punch IDs are displayed in flat pattern punch tables. See

[IView::InsertPunchTable](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~InsertPunchTable.html)

.

## See Also

[ILibraryFormToolFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFormToolFeatureData.html)

[ILibraryFormToolFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFormToolFeatureData_members.html)

## Availability

SOLIDWORKS 2025 SP02, Revision Number 33.2
