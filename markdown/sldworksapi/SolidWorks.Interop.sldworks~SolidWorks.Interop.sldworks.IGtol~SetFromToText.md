---
title: "SetFromToText Method (IGtol)"
project: "SOLIDWORKS API Help"
interface: "IGtol"
member: "SetFromToText"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~SetFromToText.html"
---

# SetFromToText Method (IGtol)

Adds a From-To symbol and sets the From-To text for this Gtol.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetFromToText( _
   ByVal EnableFromTo As System.Boolean, _
   ByVal FromText As System.String, _
   ByVal ToText As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IGtol
Dim EnableFromTo As System.Boolean
Dim FromText As System.String
Dim ToText As System.String
Dim value As System.Boolean

value = instance.SetFromToText(EnableFromTo, FromText, ToText)
```

### C#

```csharp
System.bool SetFromToText(
   System.bool EnableFromTo,
   System.string FromText,
   System.string ToText
)
```

### C++/CLI

```cpp
System.bool SetFromToText(
   System.bool EnableFromTo,
   System.String^ FromText,
   System.String^ ToText
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `EnableFromTo`: True to enable From-To symbol
- `FromText`: From text label
- `ToText`: To text label

### Return Value

True if From-To text successfully set, false if not

## VBA Syntax

See [Gtol::SetFromToText](ms-its:sldworksapivb6.chm::/sldworks~Gtol~SetFromToText.html).

## Examples

See the [IGtolFrame](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtolFrame.html) examples.

## Remarks

The From-To symbol:

- is present below the Gtol frame.
- specifies that the Gtol value applies from one point or entity to another.

## See Also

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.html)
[IGtol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.html)
[IGtol::GetFromToText Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetFromToText.html)

## Availability

SOLIDWORKS 2023 FCS, Revision Number 31
