---
title: "SetClass Method (IPropertyManagerPageActiveX)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageActiveX"
member: "SetClass"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageActiveX~SetClass.html"
---

# SetClass Method (IPropertyManagerPageActiveX)

Sets the interface to this ActiveX control.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetClass( _
   ByVal ClassID As System.String, _
   ByVal LicenseKey As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPageActiveX
Dim ClassID As System.String
Dim LicenseKey As System.String
Dim value As System.Boolean

value = instance.SetClass(ClassID, LicenseKey)
```

### C#

```csharp
System.bool SetClass(
   System.string ClassID,
   System.string LicenseKey
)
```

### C++/CLI

```cpp
System.bool SetClass(
   System.String^ ClassID,
   System.String^ LicenseKey
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ClassID`: Class ID for the control
- `LicenseKey`: License key for the control

### Return Value

Always returns true

## VBA Syntax

See [PropertyManagerPageActiveX::SetClass](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPageActiveX~SetClass.html).

## Examples

See the [IPropertyManagerPageActiveX](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageActiveX.html) examples.

## Remarks

This method sets the class ID and license key information for the ActiveX control when a PropertyManager page created using the API is shown and the ActiveX control is created. ClassId can be either the name of the control (ProgID) or the class ID (CLSID), for example, "MSCAL.calendar" or "{8E27C92B-1264-101C-8A2F-040224009C02}". Both provide the calendar protocol. You can obtain these strings using a combination of the Microsoft OLE/COM Object Viewer and the registry editor.

VBA example:

' ProgID

bRet = m_pActiveXControl.SetClass("MSCAL.Calendar", "")

bRet = m_pActiveXControl2.SetClass("MSComctlLib.ListViewCtrl", "")

' CLSID

bRet = m_pActiveXControl.SetClass("{8E27C92B-1264-101C-8A2F-040224009C02}", "")

bRet = m_pActiveXControl2.SetClass("{BDD1F04B-858B-11D1-B16A-00C0F0283628}", "")

This method does not check to determine if the creation of the control worked. Instead, the [IPropertyManagerPage2Handler5::OnActiveXControlCreated](ms-its:swpublishedapi.chm::/SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.IPropertyManagerPage2Handler5~OnActiveXControlCreated.html) sends notification when an attempt to create the ActiveX control occurs, regardless if it is created or not. Use the IPropertyManagerPage2Handler5::OnActiveXControlCreated method's return value to indicate what action to take if the creation of the control failed.

## See Also

[IPropertyManagerPageActiveX Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageActiveX.html)
[IPropertyManagerPageActiveX Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageActiveX_members.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
