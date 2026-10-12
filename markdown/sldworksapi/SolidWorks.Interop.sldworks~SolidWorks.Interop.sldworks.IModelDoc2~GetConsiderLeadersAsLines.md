---
title: "GetConsiderLeadersAsLines Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "GetConsiderLeadersAsLines"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetConsiderLeadersAsLines.html"
---

# GetConsiderLeadersAsLines Method (IModelDoc2)

Gets whether the display data of a leader is included as lines when the lines are retrieved from a view or annotation in this document.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetConsiderLeadersAsLines() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim value As System.Boolean

value = instance.GetConsiderLeadersAsLines()
```

### C#

```csharp
System.bool GetConsiderLeadersAsLines()
```

### C++/CLI

```cpp
System.bool GetConsiderLeadersAsLines();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if leaders are returned as line data, false if leaders are not returned as line data

## VBA Syntax

See [ModelDoc2::GetConsiderLeadersAsLines](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~GetConsiderLeadersAsLines.html).

## Remarks

The various GetLeaderCount and GetLeaderAtIndex mehtods return information about where the vertices of the leader are located. These methods also return the leader information as part of its line information.

Depending on what your program is trying to accomplish and which APIs it is using, this duplication of information may not be desirable. [IModelDoc2::SetConsiderLeadersAsLines](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~SetConsiderLeadersAsLines.html) controls this behavior by setting a flag on the document that indicates whether the leader information should be returned as part of the line information. IModelDoc2::GetConsiderLeadersAsLines gets the current behavior for this document.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
