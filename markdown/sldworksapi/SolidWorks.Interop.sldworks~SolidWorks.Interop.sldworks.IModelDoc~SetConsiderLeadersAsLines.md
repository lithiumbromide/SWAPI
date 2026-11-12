---
title: "SetConsiderLeadersAsLines Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "SetConsiderLeadersAsLines"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~SetConsiderLeadersAsLines.html"
---

# SetConsiderLeadersAsLines Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::SetConsiderLeadersAsLines](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~SetConsiderLeadersAsLines.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SetConsiderLeadersAsLines( _
   ByVal LeadersAsLines As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim LeadersAsLines As System.Boolean
Dim value As System.Boolean

value = instance.SetConsiderLeadersAsLines(LeadersAsLines)
```

### C#

```csharp
System.bool SetConsiderLeadersAsLines(
   System.bool LeadersAsLines
)
```

### C++/CLI

```cpp
System.bool SetConsiderLeadersAsLines(
   System.bool LeadersAsLines
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `LeadersAsLines`:

## VBA Syntax

See [ModelDoc::SetConsiderLeadersAsLines](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~SetConsiderLeadersAsLines.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
