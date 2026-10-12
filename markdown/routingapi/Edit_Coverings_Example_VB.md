---
title: "Edit Coverings Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "routingapi/Edit_Coverings_Example_VB.htm"
---

# Edit Coverings Example (VBA)

This example shows how to edit coverings.

```vb
'----------------------------------------------
' Required reference: Microsoft Scripting Runtime
'----------------------------------------------
Sub EditCovering(ByRef rtRouteManager As SWRoutingLib.RouteManager)
    Dim vWires                      As Variant
    Dim vWire                       As Variant
    Dim rtWire                      As SWRoutingLib.Wire
    Dim vRouteSegmentIDs            As Variant
    Dim lNumRouteSegmentID          As Long
    Dim lIdx                        As Long
    Dim rtElectricalRoute           As SWRoutingLib.ElectricalRoute
    Dim rtRouteProperty             As SWRoutingLib.RouteProperty
    Dim rtElectricalRouteProperty   As SWRoutingLib.ElectricalRouteProperty
    Dim bRetVal                     As Boolean
    Dim dictSegmentsProcessed       As Scripting.Dictionary
    Dim rtCovering                  As SWRoutingLib.Covering

    ' Get the electrical route
    Set rtElectricalRoute = rtRouteManager.GetElectricalRoute

    If rtElectricalRoute Is Nothing Then
        Debug.Print "No electrical route found."
        Exit Sub
    End If

    ' Loop over all wires
    vWires = rtElectricalRoute.GetWires

    If Not IsEmpty(vWires) Then

        Set dictSegmentsProcessed = New Scripting.Dictionary

        For Each vWire In vWires

            Set rtWire = vWire

            vRouteSegmentIDs = rtWire.GetRouteSegmentIDs

            If Not IsEmpty(vRouteSegmentIDs) Then

                For lIdx = LBound(vRouteSegmentIDs) To UBound(vRouteSegmentIDs)

                    ' Get segment ID
                    lNumRouteSegmentID = vRouteSegmentIDs(lIdx)

                    ' Check to see if ID already processed
                    If Not dictSegmentsProcessed.Exists(lNumRouteSegmentID) Then

                        Debug.Print "segment id = " & lNumRouteSegmentID

                        Set rtRouteProperty = rtElectricalRoute.GetRouteProperty(lNumRouteSegmentID)

                        ' Register this property so that you know that you have already dealt with it
                        dictSegmentsProcessed.Add lNumRouteSegmentID, rtRouteProperty

                        ' If a covering is present, edit it
                        If rtRouteProperty.HasCovering Then

                            Set rtCovering = rtRouteProperty.GetCovering

                            rtCovering.Name = rtCovering.Name & "-z"
                            rtCovering.Color = RGB(255, 0, 0)
                            rtCovering.OuterDiameter = 1.1 * rtCovering.OuterDiameter
                            rtCovering.PartNumber = "0123456789ABCDEF"

                            ' No need to call RouteManager.EditWires to commit the changes

                        End If

                    End If

                Next lIdx

            End If

        Next vWire

    End If

    ' Release
    Set dictSegmentsProcessed = Nothing

End Sub
```
