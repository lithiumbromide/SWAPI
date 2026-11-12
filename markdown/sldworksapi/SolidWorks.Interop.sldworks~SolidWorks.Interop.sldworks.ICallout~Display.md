---
title: "Display Method (ICallout)"
project: "SOLIDWORKS API Help"
interface: "ICallout"
member: "Display"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout~Display.html"
---

# Display Method (ICallout)

Shows or hides the independent (i.e., not attached to a selection) callout.

## Syntax

### Visual Basic (Declaration)

```vb
Function Display( _
   ByVal Display As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICallout
Dim Display As System.Boolean
Dim value As System.Boolean

value = instance.Display(Display)
```

### C#

```csharp
System.bool Display(
   System.bool Display
)
```

### C++/CLI

```cpp
System.bool Display(
   System.bool Display
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Display`: True to show the callout, false to hide it

### Return Value

True if the operation is successful, false if not

## VBA Syntax

See [Callout::Display](ms-its:sldworksapivb6.chm::/sldworks~Callout~Display.html).

## Examples

[Create a Callout Independent of a Selection (VBA)](Create_a_Callout_Independent_of_a_Selection_Example_VB.htm)
[Create a Callout Independent of a Selection (VB.NET)](Create_a_Callout_Independent_of_a_Selection_Example_VBNET.htm)
[Create a Callout Independent of a Selection (C#)](Create_a_Callout_Independent_of_a_Selection_Example_CSharp.htm)

## See Also

[ICallout Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout.html)
[ICallout Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout_members.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
