module Main exposing (main)

import Browser
import Dict exposing (Dict)
import Html exposing (Html)
import Html.Attributes as Attr exposing (class)
import Html.Events as Html
import Http
import Json.Decode as D
import Json.Decode.Extra as D
import List
import List.Extra as List


dbDecoder : D.Decoder DB
dbDecoder =
    D.succeed (\a r -> { answer = a, reason = r })
        |> D.andMap (D.field "answer" D.string)
        |> D.andMap (D.field "reason" D.string)
        |> D.dict2 D.int
        |> D.dict


type alias DB =
    Dict String (Dict Int { answer : String, reason : String })


type alias Model =
    { answers : Dict Int String, db : DB, title : Bool }


type alias Flags =
    { db : D.Value }


type Msg
    = Answer Int String
    | Go


questions =
    Dict.fromList <|
        List.zip (List.range 1 100)
            [ ( "Would you call yourself a gigachad?", [ "Yes", "No" ] )
            , ( "How immoral is your sexual activity?", [ "Not bad", "little bad", "very bad" ] )
            , ( "Do you have rizz?", [ "Yes", "No" ] )
            , ( "How down-bad are you?", [ "I’m not", "eh", "it’s bad" ] )
            , ( "How big is your brain?", [ "small", "not of note", "big" ] )
            , ( "How do you feel about killing people?", [ "Yeah", "Nah" ] )
            , ( "Would you say you’re good with animals?", [ "Yes", "No" ] )
            , ( "You ever had 1–1 chats with God?", [ "Yes", "No" ] )
            , ( "Do you feel like an active and valued part of your community?", [ "Yes", "No" ] )
            , ( "Are you on the piss?", [ "Yes", "No" ] )
            , ( "Are you a fundamentally sad and angry kind of a person?", [ "Yes", "No" ] )
            , ( "Do you have any redeeming qualities?", [ "Yes", "No" ] )
            , ( "Would you call yourself an out of the box thinker?", [ "Yes", "No" ] )
            , ( "How much blood is on your hands?", [ "None", "a bit", "many have been struck down" ] )
            , ( "Have you ever written something which is now wrongfully included in the canon?", [ "Yes", "No" ] )
            , ( "Are you loaded?", [ "Yes", "No" ] )
            , ( "You ever feel like murdering any of your children?", [ "Yes", "No" ] )
            , ( "Do you work in the food industry?", [ "Yes", "No" ] )
            , ( "Do you work in construction?", [ "Yes", "No" ] )
            , ( "Do you work in governance?", [ "Yes", "No" ] )
            , ( "Have you lost a spouse?", [ "Yes", "No" ] )
            , ( "Do you have a cool stick?", [ "Yes", "No" ] )
            , ( "Do you keep your word?", [ "Yes", "No" ] )
            , ( "Are you straight?", [ "Yes", "No" ] )
            , ( "Would you call yourself an artistic person?", [ "Yes", "No" ] )
            , ( "Do you have two nuts?", [ "Yes", "No" ] )
            , ( "Do you have magical weirdo vibes?", [ "Yes", "No" ] )
            , ( "Have you ever experienced divine judgement?", [ "Yes", "No" ] )
            , ( "Are you a bit of a whinger?", [ "Yes", "No" ] )
            , ( "Are you a quick runner?", [ "Yes", "No" ] )
            , ( "Are you a fan of Persia?", [ "Yes" ] )
            , ( "Do you travel often?", [ "Yes", "No" ] )
            ]


main : Program Flags Model Msg
main =
    Browser.element
        { init = init
        , view = view
        , update = update
        , subscriptions = subscriptions
        }


init : Flags -> ( Model, Cmd Msg )
init f =
    ( { answers = Dict.empty, db = D.decodeValue dbDecoder f.db |> Result.withDefault Dict.empty, title = True }, Cmd.none )


ifThenElse a b c =
    if a then
        b

    else
        c


view : Model -> Html Msg
view m =
    let
        q =
            List.find (\( k, _ ) -> Dict.get k m.answers == Nothing) (Dict.toList questions)
    in
    Html.div
        [ class "flex flex-col place-items-center bg-flu-50 space-y-4 min-h-screen w-full" ]
    <|
        if m.title then
            [ Html.div [ class "mt-16 text-3xl" ] [ Html.text "Bible Character Quiz!" ]
            , Html.div [ class "text-xl" ] [ Html.text "Which bible character are you most like?" ]
            , Html.div [] []
            , Html.div [] []
            , Html.div [ class "p-4 text-xl cursor-pointer hover:bg-flu-300 border border-flu-300 rounded-lg select-none", Html.onClick Go ] [ Html.text "begin" ]
            ]

        else
            case q of
                Nothing ->
                    [ Html.div [ class "text-lg my-4" ] [ Html.text "You're most like" ]
                    , Html.div [ class "flex flex-col items-start justify-center gap-2" ] <|
                        let
                            anslst =
                                Dict.toList m.db
                                    |> List.map (\( name, ans ) -> Dict.map (\k v -> ifThenElse (Dict.get k m.answers == Just v.answer) 1 0) ans |> Dict.values |> List.sum |> Tuple.pair ( name, ans ))
                                    |> List.sortBy (Tuple.second >> (*) -1)
                        in
                        [ List.head (List.map Tuple.first anslst)
                            |> Maybe.map Tuple.first
                            |> Maybe.andThen (\x -> Dict.get x m.db |> Maybe.map (Tuple.pair x))
                            |> Maybe.map
                                (\( name, d ) ->
                                    Dict.toList d
                                        |> List.map
                                            (\( k, v ) ->
                                                let
                                                    you_ans =
                                                        Dict.get k m.answers |> Maybe.withDefault "N/A"
                                                in
                                                Html.div
                                                    [ class "flex gap-4" ]
                                                    [ Html.div [ class <| "text-center w-14 text-lg rounded-md " ++ ifThenElse (you_ans == v.answer) "bg-hl-11" "bg-hl-1" ] [ Html.text <| "Q" ++ String.fromInt k ]
                                                    , Html.div []
                                                        [ Html.div [] [ Html.text <| "You: " ++ you_ans ]
                                                        , Html.div [] [ Html.text <| "Them: " ++ v.answer ]
                                                        , Html.div [] [ Html.text v.reason ]
                                                        ]
                                                    ]
                                            )
                                        >> (++) [ Html.div [ class "text-2xl text-center mb-8 w-full" ] [ Html.text name ] ]
                                )
                            |> Maybe.withDefault [ Html.text "No one!" ]
                            |> Html.div [ class "flex flex-col gap-1" ]
                        , Html.div [ class "mt-16 w-full flex flex-col gap-2" ] (List.map (\( ( name, _ ), score ) -> Html.div [ class "text-center" ] [ Html.text <| name ++ " : " ++ String.fromInt score ]) anslst)
                        ]
                    ]

                Just ( k, ( str, opts ) ) ->
                    [ Html.div [ class "text-2xl mt-16 mb-8 hover:text-orange-600" ] [ Html.text str ]
                    , Html.div [ class "flex items-start justify-center gap-4" ] <|
                        List.map (\o -> Html.div [ class "p-4 text-xl cursor-pointer hover:bg-flu-300 border border-flu-300 rounded-lg select-none", Html.onClick (Answer k o) ] [ Html.text o ]) opts
                    ]


update : Msg -> Model -> ( Model, Cmd Msg )
update msg m =
    case msg of
        Answer i a ->
            ( { m | answers = Dict.insert i a m.answers }, Cmd.none )

        Go ->
            ( { m | title = False }, Cmd.none )


subscriptions : Model -> Sub Msg
subscriptions _ =
    Sub.none
